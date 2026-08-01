# AISKG Section 1 — literature retrieval to semantic extraction

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/romenmeitei/AISKG_01_Framework/blob/main/Mushroom_KG_Upstream_Literature_to_Extraction_Pipeline_v1.ipynb)

This repository contains the upstream literature-to-extraction component of the
AI-assisted ontology-guided semantic knowledge-graph study on mushroom
poisoning. It is followed by the deterministic post-extraction analyses in
[AISKG Section 2](https://github.com/romenmeitei/AISKG_02_Framework).

## Canonical notebook

`Mushroom_KG_Upstream_Literature_to_Extraction_Pipeline_v1.ipynb`

### `MANUSCRIPT_SNAPSHOT` — authoritative deterministic route

This default mode avoids live bibliographic APIs and transformer downloads. It
verifies the frozen input bundle, replays expert topic consolidation,
regenerates ontology-guided entity and relation tables, compares principal
outputs with frozen references, and creates the exact input bundle accepted by
Section 2.

| Expected snapshot result | Value |
|---|---:|
| Full deduplicated corpus | 2,687 records |
| Include/partial corpus | 1,868 records |
| Expert-reviewed topics | 56 |
| Consolidated research domains | 9 |
| Entity mentions | 8,292 |
| Unique canonical entities | 92 |
| Documents containing entities | 1,521 |
| Explicit sentence-level relations | 1,324 |
| Aggregated typed relations | 183 |
| Relations with support ≥2 | 86 |
| Active nodes in the support ≥2 graph | 40 |

### `LIVE_REFRESH` — optional current database update

This route contains executable code for PubMed, Scopus, and Web of Science
retrieval; harmonization and hierarchical deduplication; SentenceTransformer
embeddings; UMAP; HDBSCAN; BERTopic; expert topic review; and ontology-guided
entity/relation extraction. Live results may differ from the historical study
snapshot because databases, indexing, APIs, entitlements, and model versions
change.

The live route is split into `RETRIEVE_AND_MODEL` and
`APPLY_CURATION_AND_EXTRACT` so that human topic review remains explicit.

## Run in Google Colab

1. Open the notebook using the badge above.
2. Keep `RUN_MODE = "MANUSCRIPT_SNAPSHOT"`.
3. Select **Runtime → Run all**.
4. The notebook downloads `Mushroom_KG_Upstream_Inputs_v1.zip` from this
   repository when possible; a manual upload fallback is available.
5. Download both generated archives.
6. Supply `Mushroom_KG_Reproducibility_Inputs_v2_from_upstream.zip` to the
   Section 2 notebook.

## Live credentials

Store `ENTREZ_EMAIL`, optional `NCBI_API_KEY`, `SCOPUS_API_KEY`, `WOS_API_KEY`,
and optional `HF_TOKEN` in Google Colab Secrets or environment variables. The
pipeline does not write credentials to outputs.

## Key files

| Path | Purpose |
|---|---|
| `Mushroom_KG_Upstream_Literature_to_Extraction_Pipeline_v1.ipynb` | Canonical Colab notebook |
| `Mushroom_KG_Upstream_Inputs_v1.zip` | Frozen checksum-verified manuscript snapshot |
| `upstream_core.py` | Matching command-line implementation |
| `requirements_snapshot.txt`, `requirements_live.txt` | Dependency ranges |
| `queries/` | Exact database query text |
| `reference_outputs/` | Executed reference notebook and output archive |
| `TEST_STATUS.md`, `TESTED_ENVIRONMENT.txt`, `RELEASE_VALIDATION_REPORT.md` | Test evidence |
| `REPRODUCIBILITY_SCOPE.md` | Snapshot versus live boundaries |
| `SECTION_1_TO_SECTION_2_WORKFLOW.md` | Verified handoff to Section 2 |
| `PACKAGE_MANIFEST.csv`, `SHA256SUMS.txt` | File inventory and hashes |
| `CITATION.cff` | Machine-readable citation metadata |
| `LICENSE`, `COPYRIGHT.md`, `DATA_LICENSE.md` | Rights and reuse terms |

## Verify locally

```bash
python verify_repository.py
sha256sum -c SHA256SUMS.txt
```

## Run locally

```bash
unzip Mushroom_KG_Upstream_Inputs_v1.zip -d upstream_inputs
python upstream_core.py --mode MANUSCRIPT_SNAPSHOT \
  --input-dir upstream_inputs --output-dir upstream_outputs
```

## Public-data warning

The frozen input contains bibliographic fields from public and licensed
sources. Review `THIRD_PARTY_DATA_NOTICE.md` before public redistribution. If a
provider's terms prohibit unrestricted distribution, place the affected
snapshot in controlled access while keeping the code, exact queries, hashes,
and derived outputs public.

## Release and citation

This publication package is version **1.0.0**. Create the GitHub release tag
`v1.0.0`, archive it in a DOI-issuing repository, and then add the DOI to
`CITATION.cff` and the manuscript. Original software is MIT-licensed.
