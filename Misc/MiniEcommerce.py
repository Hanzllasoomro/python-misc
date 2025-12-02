import os
import zipfile

# Define project structure
base_path = "/mnt/data/mini-ecommerce"
folders = [
    "css",
    "js",
    "admin"
]
files_content = {
    "config.php": """<?php
$host = "localhost";
$user = "root";
$pass = "";
$db   = "mini_ecommerce";

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>""",

    "index.php": """<?php
session_start();
include 'config.php';

$result = $conn->query("SELECT * FROM products");
?>
<!DOCTYPE html>
<html>
<head>
    <title>Mini E-Commerce</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
<h1>Products</h1>
<div class="products">
    <?php while($row = $result->fetch_assoc()) { ?>
        <div class="product">
            <img src="<?= $row['image'] ?>" width="150">
            <h2><?= $row['name'] ?></h2>
            <p>$<?= $row['price'] ?></p>
            <a href="cart.php?action=add&id=<?= $row['id'] ?>">Add to Cart</a>
        </div>
    <?php } ?>
</div>
<a href="cart.php">Go to Cart</a>
</body>
</html>""",

    "cart.php": """<?php
session_start();
include 'config.php';

if (!isset($_SESSION['cart'])) {
    $_SESSION['cart'] = [];
}

if (isset($_GET['action']) && $_GET['action'] == 'add') {
    $id = $_GET['id'];
    if (!isset($_SESSION['cart'][$id])) {
        $_SESSION['cart'][$id] = 1;
    } else {
        $_SESSION['cart'][$id]++;
    }
}

if (isset($_GET['action']) && $_GET['action'] == 'remove') {
    $id = $_GET['id'];
    unset($_SESSION['cart'][$id]);
}

$total = 0;
?>
<!DOCTYPE html>
<html>
<head>
    <title>Cart</title>
</head>
<body>
<h1>Your Cart</h1>
<table border="1">
    <tr><th>Product</th><th>Quantity</th><th>Price</th><th>Action</th></tr>
    <?php foreach($_SESSION['cart'] as $id => $qty) {
        $result = $conn->query("SELECT * FROM products WHERE id=$id");
        $row = $result->fetch_assoc();
        $subtotal = $row['price'] * $qty;
        $total += $subtotal;
    ?>
        <tr>
            <td><?= $row['name'] ?></td>
            <td><?= $qty ?></td>
            <td>$<?= $subtotal ?></td>
            <td><a href="cart.php?action=remove&id=<?= $id ?>">Remove</a></td>
        </tr>
    <?php } ?>
</table>
<h2>Total: $<?= $total ?></h2>
<a href="checkout.php">Proceed to Checkout</a>
</body>
</html>""",

    "checkout.php": """<?php
session_start();
$total = 0;
include 'config.php';

if (isset($_SESSION['cart'])) {
    foreach($_SESSION['cart'] as $id => $qty) {
        $result = $conn->query("SELECT * FROM products WHERE id=$id");
        $row = $result->fetch_assoc();
        $total += $row['price'] * $qty;
    }
}
$_SESSION['cart'] = []; // Clear cart after checkout
?>
<!DOCTYPE html>
<html>
<head>
    <title>Checkout</title>
</head>
<body>
<h1>Checkout Complete</h1>
<p>Your total purchase is: $<?= $total ?></p>
<p>Thank you for shopping!</p>
<a href="index.php">Back to Shop</a>
</body>
</html>""",

    "css/style.css": """body { font-family: Arial; margin: 20px; }
.products { display: flex; gap: 20px; flex-wrap: wrap; }
.product { border: 1px solid #ddd; padding: 10px; width: 200px; text-align: center; }""",

    "admin/add_product.php": """<?php
include '../config.php';

if ($_POST) {
    $name = $_POST['name'];
    $price = $_POST['price'];
    $image = $_POST['image'];

    $conn->query("INSERT INTO products (name, price, image) VALUES ('$name', '$price', '$image')");
    header("Location: product_list.php");
}
?>
<form method="post">
    <input type="text" name="name" placeholder="Product Name"><br>
    <input type="text" name="price" placeholder="Price"><br>
    <input type="text" name="image" placeholder="Image URL"><br>
    <button type="submit">Add Product</button>
</form>""",

    "admin/product_list.php": """<?php
include '../config.php';
$result = $conn->query("SELECT * FROM products");
?>
<h1>Admin - Product List</h1>
<a href="add_product.php">Add New Product</a>
<table border="1">
<tr><th>ID</th><th>Name</th><th>Price</th><th>Image</th></tr>
<?php while($row = $result->fetch_assoc()) { ?>
<tr>
    <td><?= $row['id'] ?></td>
    <td><?= $row['name'] ?></td>
    <td>$<?= $row['price'] ?></td>
    <td><img src="<?= $row['image'] ?>" width="80"></td>
</tr>
<?php } ?>
</table>""",

    "db.sql": """CREATE DATABASE mini_ecommerce;
USE mini_ecommerce;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    image VARCHAR(255) NOT NULL
);
"""
}

# Create directories
os.makedirs(base_path, exist_ok=True)
for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Create files
for path, content in files_content.items():
    file_path = os.path.join(base_path, path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(content)

# Create ZIP file
zip_path = "/mnt/data/mini-ecommerce.zip"
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for root, dirs, files in os.walk(base_path):
        for file in files:
            zipf.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file), base_path))

zip_path
