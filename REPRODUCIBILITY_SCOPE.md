# Reproducibility scope

## Exact manuscript reproduction

`MANUSCRIPT_SNAPSHOT` is deterministic from the supplied frozen inputs. It starts from the deduplicated study corpus with the original BERTopic topic assignments, replays expert topic consolidation, and independently regenerates the initial entity and relation extraction layer. This is the authoritative route for the numerical manuscript snapshot.

The snapshot does not pretend that a live 2026 database query can recreate a historical result set exactly. Instead, it preserves the frozen corpus, expert decisions, ontology, sentence-boundary manifest, reference outputs, and checksums required to audit the published workflow.

## Complete live workflow

`LIVE_REFRESH` provides executable database-to-extraction code. It supports fresh PubMed retrieval and optional licensed Scopus and Web of Science retrieval, followed by deduplication, embedding, UMAP, HDBSCAN, BERTopic, expert curation, and ontology-guided extraction.

Live results may differ because:

- databases add, remove, or correct records;
- indexing terms and abstracts change;
- API quotas and institutional entitlements differ;
- transformer and clustering libraries evolve; and
- a newly fitted BERTopic model requires a new expert-curation decision set.

## Human curation checkpoint

Topic consolidation is not silently automated. A live model run exports a review template. Experts must label each topic and assign include/partial/exclude decisions before semantic extraction continues. BERTopic outlier topic `-1`, when retained, is explicitly excluded rather than causing a missing-review failure.

## Frozen sentence boundaries

The original extraction used spaCy sentence boundaries. Sentence segmentation can change across model versions, affecting which entity pairs are eligible for sentence-level relations. The exact snapshot therefore stores only the entity-bearing sentence boundaries from the original run. Entity mentions are regenerated from the frozen corpus and ontology; the boundary manifest prevents version-related segmentation drift.

## Section 2 handoff

The upstream pipeline writes a complete Section 2 input ZIP. The four regenerated files are audited against frozen references; static validation and held-out benchmark files are separately checksummed. The bridge manifest records the actual bytes generated in the current compatible environment, while Section 2 independently verifies 94 fixed numerical outcomes.
