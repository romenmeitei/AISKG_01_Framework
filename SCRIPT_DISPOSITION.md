# Disposition of the supplied notebooks

The original uploaded notebooks remain useful for provenance, but they should not all appear as competing runnable entry points in the public repository.

| Supplied notebook | Canonical disposition |
|---|---|
| `NLP_Mushroom_2026.ipynb` | PubMed/Scopus/WoS retrieval, metadata normalization, deduplication, BERTopic parameters, and expert-review-template logic merged into Section 1. Archive the original under `archive/legacy_notebooks/`. |
| `NLP_Mushroom_2026_Stage_II.ipynb` | Expert topic consolidation and final-theme tables merged into Section 1. Archive the original. |
| `Mushroom_Knowledge_Graph_Stage_IV_VIII.ipynb` | Entity lexicon, phrase matching, negation, relation rules, and edge aggregation merged into Section 1. Its later graph/validation cells are superseded by Section 2. |
| `Mushroom_KG_Advanced_Q1_Analyses.ipynb` | Manuscript-facing network and priority analyses superseded by Section 2. Archive for provenance. |
| `Mushroom_StageV_Advanced_Knowledge_Discovery.ipynb` | Superseded by Section 2. |
| `Mushroom_StageVI_Semantic_Validation.ipynb` | Superseded by Section 2. |
| `Mushroom_StageVII_Outcome_Aware_Validation.ipynb` | Outcome-aware refinement logic incorporated into Section 2; unsupported hard-coded result blocks should not be retained as canonical. |
| `Mushroom_StageVIII_Enhanced_Validation.ipynb` | Expert-validation sampling, agreement, adjudication, and intervals incorporated into Section 2. |
| `Statistics.ipynb` | Manuscript-facing statistics reproduced in Sections 1 and 2; archive unless an additional analysis is later identified. |

Only these two notebooks should be presented as the primary workflows:

1. `01_upstream/Mushroom_KG_Upstream_Literature_to_Extraction_Pipeline_v1.ipynb`
2. `02_post_extraction/Mushroom_KG_Complete_Reproducibility_Pipeline_v2.ipynb`
