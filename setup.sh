# Setup script for compiling the internship report
# Usage: ./setup.sh

echo "Setting up environment for LaTeX compilation..."

# Check if pdflatex is installed
if ! command -v pdflatex &> /dev/null; then
    echo "Error: pdflatex not found. Please install a LaTeX distribution (e.g., TeX Live)."
    echo "On Ubuntu/Debian: sudo apt-get install texlive-full"
    echo "On macOS: brew install --cask mactex"
    exit 1
fi

# Check if bibtex is installed
if ! command -v bibtex &> /dev/null; then
    echo "Error: bibtex not found. Please install a LaTeX distribution."
    exit 1
fi

echo "LaTeX environment detected successfully!"

# Create compilation script
cat > compile_report.sh << 'EOF'
#!/bin/bash

echo "Compiling Internship Report..."

# Clean previous compilation files
rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot

# First compilation
echo "Running first pdflatex compilation..."
pdflatex Internship_Report_3D_PointCloud_Segmentation.tex

# Process bibliography
echo "Processing bibliography..."
bibtex Internship_Report_3D_PointCloud_Segmentation

# Second compilation (resolve citations)
echo "Running second pdflatex compilation..."
pdflatex Internship_Report_3D_PointCloud_Segmentation.tex

# Third compilation (resolve cross-references)
echo "Running final pdflatex compilation..."
pdflatex Internship_Report_3D_PointCloud_Segmentation.tex

# Clean auxiliary files
echo "Cleaning auxiliary files..."
rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot

echo "Compilation complete! PDF generated: Internship_Report_3D_PointCloud_Segmentation.pdf"
EOF

chmod +x compile_report.sh

echo "Setup complete!"
echo ""
echo "To compile the report, run:"
echo "  ./compile_report.sh"
echo ""
echo "Required LaTeX packages:"
echo "  - geometry, fancyhdr, titlesec, tocloft"
echo "  - amsmath, amsfonts, amssymb"
echo "  - graphicx, booktabs, longtable, array"
echo "  - listings, xcolor, hyperref, cite"
echo "  - setspace, caption, subcaption"
echo ""
echo "If you encounter missing package errors, install them via your LaTeX distribution."
