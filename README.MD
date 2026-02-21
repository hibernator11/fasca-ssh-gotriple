# Fasca SSH example
This work intends to provide examples of use based on the [GoTriple platform](https://www.gotriple.eu/), which provides a single access point to discover and reuse open scholarly Social Sciences and Humanities (SSH) resources and find peers. The work was performed by a multidisciplinary team with researchers of different backgrounds.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hibernator11/fasca-ssh-gotriple/HEAD)

## Auhors

- Elena Battaner, Universidad Rey Juan Carlos
- Gustavo Candela, Universidad de Alicante
- Cezary Rosiński, Institute of Literary Research of the Polish Academy of Sciences
- Paul Spence, King’s College London
- Nikodem Wolczuk, Institute of Literary Research of the Polish Academy of Sciences

## Introduction

A selection of datasets were extracted from GoTriple using its API. Several topics were employed to query the system and retrieve JSON files as output. The topics employed to retrieve the data were "Race, ethnicity, and decolonization" and "Digital Humanities". Then, previous work concerning dirversity analysis of metadata was employed to perform an experiment to assess the diversity of the metadata fields keywords and language.

Diversity indices can be useful to avoid silences and biases in data, as recommended by best practices and guidelines (e.g., Collections as Data and CARE principles). This is interesting for the research community as a way to provide a transparent method to measure diversity but also to create awareness of these type of data issues.

After an analysis of the metatada fields provided by each of the results, a selection of fields were extracted to apply the diversity index: i) keywords; and language. For the analysis a period of time were established between 1998 and 2020. Since GoTriple is a multilingual repository, keywords are provided in several languages. As a result, we focused our analysis on particular languages (e.g., Spanish and English) to measure the diversity of keywords. The information about the language for keywords is not provided so we use an open software library to detect the language selected for the analysis. The following figure shows a selection of plots showing how the diversity and richness change over time.

<img src="plots/diversity.png" width="50%">

## Code

This code requires the following folders:

- input: json files
- plots: outputs to illustrate the diversity
- A Jupyter Notebook is included describing the code and process: [Diversity-FASCA-GoTriple](https://github.com/hibernator11/fasca-ssh-gotriple/blob/main/Diversity-FASCA-GoTriple.ipynb)

The code analyses the diversity of the in_language and keywords fields. Note that the GoTriple API only retrieves 10.000 records per query.

## Installation guide
The code can be run on cloud services such as [Binder](https://mybinder.org/) without the need to install additional software and using only the web browser by clicking on the link provided at the beginning of this documentation.

The code can be also installed in a computer by following these steps:
- download the code from GitHub
- open the folder with the code
- run the command: pip install -r requirements.txt
- open Jupyter (or Anaconda)
- open the notebook provided: Diversity-FASCA-GoTriple.ipynb

## Licence
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />Content is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International license</a>.

Please, note that the datasets used in this project have separate licences.

## Acknowledgments
This work is part of the FASCA initiative aiming at enriching GoTriple’s advanced services. FASCA has received funding through the OSCARS project via the European Commission’s Horizon Europe Research and Innovation programme under grant agreement No. 101129751. We would like to thank Rafael Carrasco for his idea to apply diversity indexes to metatada and content.

### References
- C. Carrasco, R., Candela, G. & Marco-Such, M. Measuring the diversity of data and metadata in digital libraries. Int J Digit Libr 26, 5 (2025). https://doi.org/10.1007/s00799-025-00411-1
- Hill, M. O. 1973. Diversity and Evenness: A Unifying Notation and Its Consequences. Ecology 54 (2): 427432. https://doi.org/10.2307/1934352
- Alkemade, H., Candela, G., Claeyssens, S., Colavizza, G., Eren, S., Freire, N., Irollo, A., Isaac, A., Lehmann, J., Neudecker, C., Osti, G., van Strien, D., & Wevers, M. (2025). Datasheets for Digital Cultural Heritage Datasets (Versión 2). Zenodo. https://doi.org/10.5281/zenodo.15828222
- Padilla, T., Scates Kettler, H., Varner, S., & Shorish, Y. (2023). Vancouver Statement on Collections as Data. Zenodo. https://doi.org/10.5281/zenodo.8342171
- Carroll, S., Garba, I., Figueroa-Rodriguez, O., Holbrook, J., Lovett, R., Materechera, S., Parsons, M., Raseroka, K., Rodriguez-Lonebear, D., Rowe, R., Sara, R., Walker, J., Anderson, J., & Hudson, M. (2020). The CARE principles for Indigenous data governance. Data Science Journal, 19. https://doi.org/10.5334/dsj-2020-043
