# Name of manuscript
manuscript = phdthesis

# Source files
sources = $(wildcard *.tex) references.bib

# PdfLaTeX compilation options
latexopt = -halt-on-error -file-line-error

#=================================================================
# Generate PDF of manuscript using PdfLaTeX
#=================================================================

all: $(manuscript).pdf

$(manuscript).pdf: $(sources)
	pdflatex $(latexopt) $(manuscript).tex
	bibtex -terse $(manuscript).aux
	pdflatex $(latexopt) $(manuscript).tex
	pdflatex $(latexopt) $(manuscript).tex

#=================================================================
# Generate Images
#=================================================================

#=================================================================
# Other
#=================================================================

clean:
	@rm -f *.aux *.bbl *.blg *.log *.out *.spl *.lof *.lot *.toc \
	$(manuscript).pdf

.PHONY: all clean
