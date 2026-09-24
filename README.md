# E-Commerce Customer & Order Analytics

## 1. Problem Statement
The objective of this project is to analyze online customer behavior, the impact of discounting strategies, and the logistical efficiency of deliveries. The e-commerce platform needs actionable insights to optimize profitability and improve customer satisfaction.

## 2. Objectives
- Segment customers by value and determine which tier contributes the most revenue.
- Analyze regional sales performance.
- Investigate the threshold where discounts begin to negatively impact overall profit.
- Map delivery performance (days to deliver) against customer satisfaction (ratings).

## 3. Dataset Description
- **Type**: Self-generated synthetic dataset created specifically for this project.
- **Records**: 1,250 realistic e-commerce orders.
- **Fields**: Order_ID, Order_Date, Customer_ID, Customer_Segment, Age, Gender, Region, Product_ID, Product_Name, Category, Quantity, Unit_Price, Discount, Shipping_Cost, Payment_Method, Delivery_Days, Order_Status, Customer_Rating, Cost, Revenue, Profit.

## 4. Technologies & Libraries
- **Language**: Python
- **Libraries**: `pandas`, `numpy`, `streamlit`, `plotly`
- **Dashboard Framework**: Streamlit

## 5. Project Structure
```
Project_2/
├── project_2.py              # Main Streamlit dashboard application
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── Project_2_Report.docx     # Comprehensive business report
└── data/
    └── ecommerce_orders_2.csv # Synthetic dataset
```

## 6. Installation & Execution
1. Ensure Python 3.8+ is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the dashboard:
   ```bash
   streamlit run project_2.py
   ```

## 7. Dashboard Instructions
- The dashboard is divided into three main tabs: Customer Behavior, Product/Discount Profitability, and Delivery/Logistics.
- Use the sidebar filters to drill down into specific Regions or Customer Segments.
- The KPIs at the top will dynamically update based on your filter selections.

## 8. KPIs & Analytical Questions
**KPIs Monitored:** Total Revenue, Total Profit, Total Orders, Average Order Value (AOV).
**Questions Answered:**
- Which customer segment contributes the most to overall profitability?
- At what threshold do discounts begin to negatively impact overall profit?
- How does delivery time impact customer ratings and the likelihood of returns?

## 9. Key Findings
- **Premium Customers** generate a disproportionately large share of total revenue compared to Occasional buyers.
- **Excessive Discounting in the South Region** is eroding profit margins, frequently resulting in a net loss per transaction.
- **Delivery Delays** greater than 7 days show a stark correlation with a drop in customer satisfaction ratings and an increase in return status.

## 10. Business Recommendations
1. **Discount Optimization:** Cap promotional discounts at 20% in the South region to protect gross margins.
2. **Logistics Overhaul:** Renegotiate contracts with last-mile logistics partners for the West region to ensure delivery times are kept strictly under 7 days.
3. **VIP Program:** Introduce a dedicated VIP loyalty tier to nurture the 'Premium' segment and encourage more frequent purchasing behavior.

## 11. Limitations & Conclusion
**Limitations**: The dataset is entirely synthetic. Real-world e-commerce data often requires handling complex issues like split shipments, partial refunds, and fraudulent transactions.
**Conclusion**: By mapping delivery times to satisfaction and discounts to profitability, management can stop revenue leakage and dramatically improve the lifetime value of their customers.
