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
