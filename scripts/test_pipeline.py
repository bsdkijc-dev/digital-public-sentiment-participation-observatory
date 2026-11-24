import unittest
from pii_scrubber import scrub_pii, contains_pii
from social_listening_pipeline import load_taxonomy, classify_topic, classify_sentiment, process_records


class TestDSPPOPipeline(unittest.TestCase):
    def test_pii_scrubber(self):
        raw = "Hubungi budi@example.com, NIK 3201012345678901, HP 081234567890, akun @budi_test"
        cleaned = scrub_pii(raw)
        self.assertFalse(contains_pii(cleaned))
        self.assertIn("[REDACTED_EMAIL]", cleaned)
        self.assertIn("[REDACTED_NIK]", cleaned)
        self.assertIn("[REDACTED_PHONE]", cleaned)
        self.assertIn("[REDACTED_HANDLE]", cleaned)

    def test_topic_and_sentiment(self):
        tax = load_taxonomy()
        self.assertEqual(classify_topic("Mediator harus netral dan menjaga itikad baik", tax), "TAX-03")
        self.assertEqual(classify_topic("Aplikasi e-court error saat unggah", tax), "TAX-02")
        self.assertEqual(classify_sentiment("Cepat dan membantu"), "POSITIVE")
        self.assertEqual(classify_sentiment("Proses lambat dan mahal"), "NEGATIVE")
        self.assertEqual(classify_sentiment("Cepat tapi mahal"), "MIXED")

    def test_process_records_zero_pii(self):
        out = process_records([{"record_id": "T-1", "language": "id", "text": "Email test@example.com mediasi lambat"}])
        self.assertEqual(len(out), 1)
        self.assertFalse(contains_pii(out[0]["anonymised_excerpt"]))


if __name__ == "__main__":
    unittest.main()
