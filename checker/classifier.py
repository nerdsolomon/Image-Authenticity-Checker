class ImageClassifier:
    def __init__(self, similarity_threshold=85):
        self.similarity_threshold = similarity_threshold

    def classify(self, similarity_results, exif_data):
        max_similarity = max(
            (item["similarity"] for item in similarity_results),
            default=0
        )

        if max_similarity >= self.similarity_threshold:
            return "Suspicious Image"

        if exif_data is None or len(exif_data) == 0:
            return "Suspicious Image"

        return "Likely Original"
