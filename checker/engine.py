class ImageAuthenticityEngine:
    def __init__(self, hasher, similarity_checker, exif_reader, classifier):
        self.similarity_checker = similarity_checker
        self.exif_reader = exif_reader
        self.classifier = classifier

    def analyze(self, image_path, reference_dir):
        similarities = self.similarity_checker.compare_with_directory(
            image_path, reference_dir
        )

        exif_data = self.exif_reader.extract(image_path)
        verdict = self.classifier.classify(similarities, exif_data)

        return {
            "similarities": similarities,
            "exif": exif_data,
            "verdict": verdict
        }
