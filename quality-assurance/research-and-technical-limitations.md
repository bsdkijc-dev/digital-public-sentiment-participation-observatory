# Research and Technical Limitations (Phase 0 Audit)

1. **Non-Representativeness of Social Media**: Online discourse skews toward urban, digitally connected, and vocal users; findings must never be extrapolated as Indonesia-wide public opinion.
2. **WAF & Source Access Constraints**: Automated scraping of `putusan3.mahkamahagung.go.id` is blocked by an `HTTP/2 403` WAF challenge (`accept-ch: Sec-CH-UA-*`) and remains strictly halted per governance rules; case-level triangulation relies on manual exports, MA RI Laptah PDFs, or formal data-access requests.
3. **Sentiment Ambiguity in Legal Indonesian**: Sarcasm, regional idioms, and mixed procedural feedback (e.g., praising court staff while criticising e-Court downtime) require human-in-the-loop validation alongside automated NLP.
4. **Compute & Zero-Cost Constraints**: Dell Precision 7540 (Quadro T2000 4 GB VRAM) limits local LLM inference to compact models (`qwen2.5:3b`, `bge-m3` via Ollama) and batch processing without paid cloud APIs.
5. **No Causal Attribution**: Public discourse trends do not establish causal regulatory impact; causal claims require formal ex-post RIA triangulation within IJRIO.
6. **Institutional Independence**: DSPPO has no official mandate from Mahkamah Agung RI; institutional policy responses in Stage 6 remain advisory unless formally adopted.
