#!/usr/bin/env python3
"""
Project verification script.
Verifies that all required files are present in the project.
"""

import os
from pathlib import Path
from typing import List, Tuple

# Define required files
REQUIRED_FILES = {
    "Backend": [
        "backend/app/__init__.py",
        "backend/app/main.py",
        "backend/app/database.py",
        "backend/app/wsgi.py",
        "backend/app/models/__init__.py",
        "backend/app/models/product.py",
        "backend/app/models/customer.py",
        "backend/app/models/order.py",
        "backend/app/models/order_item.py",
        "backend/app/routes/__init__.py",
        "backend/app/routes/products.py",
        "backend/app/routes/customers.py",
        "backend/app/routes/orders.py",
        "backend/app/schemas/__init__.py",
        "backend/requirements.txt",
        "backend/Dockerfile",
        "backend/.dockerignore",
        "backend/.env",
        "backend/.env.example",
        "backend/.env.production.example",
    ],
    "Frontend": [
        "frontend/src/main.jsx",
        "frontend/src/App.jsx",
        "frontend/src/index.css",
        "frontend/src/pages/Dashboard.jsx",
        "frontend/src/pages/Products.jsx",
        "frontend/src/pages/Customers.jsx",
        "frontend/src/pages/Orders.jsx",
        "frontend/src/components/Layout.jsx",
        "frontend/src/components/StatCard.jsx",
        "frontend/src/services/api.js",
        "frontend/package.json",
        "frontend/vite.config.js",
        "frontend/tailwind.config.js",
        "frontend/postcss.config.js",
        "frontend/index.html",
        "frontend/Dockerfile",
        "frontend/.dockerignore",
        "frontend/.npmignore",
        "frontend/.env.local",
        "frontend/.env.production",
        "frontend/.env.example",
    ],
    "Configuration": [
        "docker-compose.yml",
        ".gitignore",
        "setup.sh",
        "setup.bat",
        "Makefile",
        "init_db.py",
    ],
    "Documentation": [
        "README.md",
        "QUICKSTART.md",
        "DEPLOYMENT.md",
        "API_EXAMPLES.md",
        "IMPLEMENTATION_SUMMARY.md",
    ],
}


def verify_files() -> Tuple[bool, List[str], List[str]]:
    """
    Verify that all required files exist.
    
    Returns:
        Tuple of (all_exist: bool, existing_files: List, missing_files: List)
    """
    project_root = Path(__file__).parent
    existing = []
    missing = []
    
    for category, files in REQUIRED_FILES.items():
        for file_path in files:
            full_path = project_root / file_path
            if full_path.exists():
                existing.append(f"✅ {file_path}")
            else:
                missing.append(f"❌ {file_path}")
    
    return len(missing) == 0, existing, missing


def print_results(all_exist: bool, existing: List[str], missing: List[str]):
    """Print verification results."""
    print("\n" + "=" * 70)
    print("📋 PROJECT VERIFICATION REPORT")
    print("=" * 70)
    
    print(f"\n📊 STATISTICS:")
    print(f"  Total files checked: {len(existing) + len(missing)}")
    print(f"  Files found: {len(existing)}")
    print(f"  Files missing: {len(missing)}")
    
    if all_exist:
        print("\n✅ ALL FILES VERIFIED - Project is complete!\n")
    else:
        print("\n⚠️  MISSING FILES DETECTED:\n")
        for file in missing:
            print(f"  {file}")
        print()
    
    # Detailed breakdown by category
    print("\n📁 DETAILED BREAKDOWN:\n")
    
    for category, files in REQUIRED_FILES.items():
        category_files = [f for f in existing if any(f for file in files if file in f)]
        total = len(files)
        found = len([f for f in category_files if "✅" in f])
        
        percentage = (found / total * 100) if total > 0 else 0
        status = "✅" if found == total else "⚠️"
        
        print(f"{status} {category}: {found}/{total} ({percentage:.0f}%)")
    
    print("\n" + "=" * 70)
    
    if all_exist:
        print("\n🎉 PROJECT IS READY FOR DEVELOPMENT!\n")
        print("Next steps:")
        print("  1. Review QUICKSTART.md for quick start")
        print("  2. Run: docker-compose up --build")
        print("  3. Access: http://localhost:5173\n")
    else:
        print("\n❌ PLEASE CREATE MISSING FILES BEFORE PROCEEDING\n")


def main():
    """Run verification."""
    print("\n🔍 Verifying project structure...\n")
    all_exist, existing, missing = verify_files()
    print_results(all_exist, existing, missing)
    
    return 0 if all_exist else 1


if __name__ == "__main__":
    exit(main())
