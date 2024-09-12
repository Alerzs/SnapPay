SnapFood Payment System
This Django app manages payment processing for SnapFood, handling coupons, invoices (factors), and transactions.

Key Features
.Coupon (Copun) Management: Create and apply discount coupons for users.
.Invoice (Factor) Management: Track and manage invoices.
.Transaction Handling: Securely process payments and record transaction history.
Installation
1.Clone the repository:
git clone https://github.com/Alerzs/SnapPay
cd snapfood/payment

2.Install dependencies:
pip install -r requirements.txt

3.Apply migrations:
python manage.py migrate

4.Run the development server:
python manage.py runserver

API Endpoints
/login/: JWT login.
/copun/: View and create coupons.
/edcopun/<int:pk>/: Edit or delete a coupon.
/add_copun/<int:pk>/: Apply a coupon to an invoice.
/trans/: Start a transaction.
/my_factors/: View invoice history.
/my_trans/: View transaction history.
Configuration
JWT Authentication: Uses JWT for securing API routes. Token lifetimes can be configured in settings.py:
python
Copy code
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
