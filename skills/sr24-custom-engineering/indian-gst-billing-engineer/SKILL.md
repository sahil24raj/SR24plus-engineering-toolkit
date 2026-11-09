---
name: indian-gst-billing-engineer
description: Architect of Indian GST compliance, multi-tier tax computation (CGST, SGST, IGST), HSN classification, B2B tax invoices, and 80mm/58mm thermal retail slips.
---

# Indian GST & Retail Billing Architecture Engineer

## Role & Mission
The **Indian GST & Retail Billing Architecture Engineer** designs and implements mathematically exact, legally compliant Indian tax calculation engines, B2B tax invoices, and high-speed B2C retail POS billing systems.

---

## 1. Activation Conditions
Invoke this skill whenever:
- Implementing GST calculations (intra-state CGST + SGST vs inter-state IGST).
- Handling HSN/SAC codes and tax slabs (0%, 5%, 12%, 18%, 28%).
- Generating compliant B2B tax invoices or thermal retail cash memos (80mm/58mm).
- Validating Indian GSTIN numbers, state codes, and Place of Supply (POS).
- Integrating tax breakdown in SaaS billing or kirana POS systems (e.g. Dukan Sathi).

---

## 2. Technical Best Practices & Mathematical Formulation

### Tax Computation Rules:
1. **Intra-State Supply** (`Supplier State Code == Buyer State Code`):
   $$\text{CGST Rate} = \frac{\text{GST Rate}}{2}, \quad \text{SGST Rate} = \frac{\text{GST Rate}}{2}, \quad \text{IGST} = 0$$
2. **Inter-State Supply** (`Supplier State Code \neq Buyer State Code`):
   $$\text{IGST Rate} = \text{GST Rate}, \quad \text{CGST} = 0, \quad \text{SGST} = 0$$
3. **Inclusive vs Exclusive Pricing**:
   - For Kirana B2C Retail, prices are almost always **GST-Inclusive** (MRP):
     $$\text{Taxable Value} = \frac{\text{Gross Amount}}{1 + \frac{\text{GST Rate}}{100}}$$
     $$\text{Total GST} = \text{Gross Amount} - \text{Taxable Value}$$

---

## 3. GSTIN Validation & Parsing Specification
An Indian GSTIN has 15 alphanumeric characters:
`22AAAAA0000A1Z5`
- `22`: 2-digit State Code (e.g. `27` Maharashtra, `07` Delhi, `10` Bihar, `29` Karnataka).
- `AAAAA0000A`: 10-character PAN of the entity.
- `1`: Entity number of the same PAN holder in the state.
- `Z`: Alphabet 'Z' by default.
- `5`: Checksum digit.

```typescript
export const GSTIN_REGEX = /^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$/;

export function validateGstin(gstin: string): { isValid: boolean; stateCode?: string } {
  const clean = gstin.trim().toUpperCase();
  if (!GSTIN_REGEX.test(clean)) {
    return { isValid: false };
  }
  return { isValid: true, stateCode: clean.slice(0, 2) };
}
```

---

## 4. Itemized Calculation Implementation
```typescript
export interface InvoiceItem {
  id: string;
  name: string;
  hsn: string;
  quantity: number;
  unitPrice: number; // MRP or base price
  gstRate: number;   // e.g. 5, 12, 18, 28
  isPriceInclusiveOfGst: boolean;
}

export function computeInvoiceTaxes(
  items: InvoiceItem[],
  supplierStateCode: string,
  buyerStateCode: string
) {
  const isInterState = supplierStateCode !== buyerStateCode;
  
  let totalTaxableValue = 0;
  let totalCgst = 0;
  let totalSgst = 0;
  let totalIgst = 0;
  let grandTotal = 0;

  const calculatedItems = items.map((item) => {
    let taxableAmount = 0;
    let taxAmount = 0;

    if (item.isPriceInclusiveOfGst) {
      const gross = item.unitPrice * item.quantity;
      taxableAmount = gross / (1 + item.gstRate / 100);
      taxAmount = gross - taxableAmount;
    } else {
      taxableAmount = item.unitPrice * item.quantity;
      taxAmount = taxableAmount * (item.gstRate / 100);
    }

    taxableAmount = Math.round(taxableAmount * 100) / 100;
    taxAmount = Math.round(taxAmount * 100) / 100;
    const itemTotal = Math.round((taxableAmount + taxAmount) * 100) / 100;

    let cgst = 0, sgst = 0, igst = 0;
    if (isInterState) {
      igst = taxAmount;
    } else {
      cgst = Math.round((taxAmount / 2) * 100) / 100;
      sgst = Math.round((taxAmount - cgst) * 100) / 100;
    }

    totalTaxableValue += taxableAmount;
    totalCgst += cgst;
    totalSgst += sgst;
    totalIgst += igst;
    grandTotal += itemTotal;

    return {
      ...item,
      taxableAmount,
      cgst,
      sgst,
      igst,
      total: itemTotal,
    };
  });

  // Round-off handling to nearest rupee
  const roundedGrandTotal = Math.round(grandTotal);
  const roundOff = Math.round((roundedGrandTotal - grandTotal) * 100) / 100;

  return {
    items: calculatedItems,
    isInterState,
    totalTaxableValue: Math.round(totalTaxableValue * 100) / 100,
    totalCgst: Math.round(totalCgst * 100) / 100,
    totalSgst: Math.round(totalSgst * 100) / 100,
    totalIgst: Math.round(totalIgst * 100) / 100,
    roundOff,
    grandTotal: roundedGrandTotal,
  };
}
```

---

## 5. Quality Checklist
- [ ] Round-off to exact 2 decimal places in calculations, round to 0 decimal places on final invoice total.
- [ ] Display HSN summary table grouped by HSN code (HSN, Taxable Value, CGST, SGST, Total Tax).
- [ ] Thermal print layouts support 48 characters width (80mm) and 32 characters width (58mm).
- [ ] Invoice serial numbers must be consecutive, alphanumeric, and reset annually (e.g. `DS/26-27/0001`).
