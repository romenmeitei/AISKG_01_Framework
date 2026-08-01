# AISKG Section 1 — literature retrieval to semantic extraction

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/romenmeitei/AISKG_01_Framework/blob/main/Mushroom_KG_Upstream_Literature_to_Extraction_Pipeline_v1.ipynb)

This repository contains the upstream, literature-to-extraction component of the
AI-assisted ontology-guided semantic knowledge-graph study on mushroom
poisoning. It precedes the deterministic post-extraction analyses in
[AISKG Section 2](https://github.com/romenmeitei/AISKG_02_Framework).

## Canonical entry point

`Mushroom_KG_Upstream_Literature_to_Extraction_Pipeline_v1.ipynb`

The notebook provides two execution modes.

### `MANUSCRIPT_SNAPSHOT` — default, deterministic, and tested

This mode does not contact bibliographic APIs or download a transformer model.
It verifies the frozen input bundle, replays expert topic consolidation,
regenerates ontology-guided entity and relation tables, compares them with
frozen references, and creates the exact input bundle required by Section 2.

| Snapshot result | Expected value |
|---|---:|
| Full deduplicated corpus | 2,687 records |
| Include/partial corpus | 1,868 records |
| Reviewed BERTopic topics | 56 |
| Final expert-curated domains | 9 |
| Entity mentions | 8,292 |
| Unique canonical entities | 92 |
| Documents containing entities | 1,521 |
| Explicit sentence-level relations | 1,324 |
| Aggregated typed relations | 183 |
| Relations supported by at least two documents | 86 |
| Active nodes in the support ≥2 graph | 40 |

### `LIVE_REFRESH` — optional database-to-extraction update

This mode contains executable code for PubMed, Scopus, and Web of Science
retrieval; metadata harmonization; hierarchical deduplication; SentenceTransformer
embedding; UMAP; HDBSCAN; BERTopic; expert topic review; and ontology-guided
entity and relation extraction. A live refresh will not reproduce historical
record counts exactly because databases and dependencies change over time.

The live route is split into:

1. `RETRIEVE_AND_MODEL`, which creates `16_live_topic_expert_review_template.csv`;
2. `APPLY_CURATION_AND_EXTRACT`, which applies the completed expert review and
   regenerates semantic extraction.

## Run in Google Colab

1. Open the notebook using the badge above.
2. Keep `RUN_MODE = "MANUSCRIPT_SNAPSHOT"` for the published study snapshot.
3. Select **Runtime → Run all**.
4. The notebook automatically downloads `Mushroom_KG_Upstream_Inputs_v1.zip`
   from this repository. A manual upload fallback is available.
5. Download:
   - `Mushroom_KG_Upstream_Reproducibility_Outputs.zip`
   - `Mushroom_KG_Reproducibility_Inputs_v2_from_upstream.zip`
6. Supply the second ZIP to the Section 2 notebook.

## Live-refresh credentials

Store credentials in Google Colab Secrets or environment variables:

- `ENTREZ_EMAIL` — required for PubMed;
- `NCBI_API_KEY` — optional;
- `SCOPUS_API_KEY` — required for Scopus;
- `WOS_API_KEY` — required for Web of Science;
- `HF_TOKEN` — optional for Hugging Face access.

Credentials are not written to result files.

## Repository contents

| Path | Purpose |
|---|---|
| `Mushroom_KG_Upstream_Literature_to_Extraction_Pipeline_v1.ipynb` | Canonical Colab notebook |
| `Mushroom_KG_Upstream_Inputs_v1.zip` | Frozen, checksummed manuscript input snapshot |
| `upstream_core.py` | Matching command-line implementation |
| `requirements_snapshot.txt` | Snapshot-mode dependency ranges |
| `requirements_live.txt` | Additional live-refresh dependencies |
| `queries/` | Exact PubMed, Scopus, and Web of Science query text |
| `reference_outputs/` | Executed reference notebook and reference output archive |
| `TEST_STATUS.md` | Test and determinism evidence |
| `REPRODUCIBILITY_SCOPE.md` | Exact-snapshot versus live-refresh boundaries |
| `SECTION_1_TO_SECTION_2_WORKFLOW.md` | Verified handoff to Section 2 |
| `PACKAGE_MANIFEST.csv`, `SHA256SUMS.txt` | Repository file inventory and hashes |
| `CITATION.cff` | Machine-readable software citation metadata |
| `LICENSE`, `DATA_LICENSE.md`, `NOTICE` | Code and data licensing notices |

## Verify the repository

```bash
python verify_repository.py
# or, on systems with sha256sum:
sha256sum -c SHA256SUMS.txt
```

## Local snapshot execution

```bash
unzip Mushroom_KG_Upstream_Inputs_v1.zip -d upstream_inputs
python upstream_core.py \
  --mode MANUSCRIPT_SNAPSHOT \
  --input-dir upstream_inputs \
  --output-dir upstream_outputs
```

## Data redistribution

The frozen snapshot includes bibliographic content from public and licensed
sources. Read `DATA_LICENSE.md` before redistributing or reusing the data. The
repository owner and institution should verify that public redistribution of
Scopus- and Web of Science-derived fields is permitted by the applicable
subscription and API terms.

## License and citation

Original software is licensed under the MIT License. Original author-created
annotations and derived tables are covered as described in `DATA_LICENSE.md`.
The software citation is provided in `CITATION.cff`.
