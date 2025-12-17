import os


class SimilarityChecker:
    def __init__(self, hasher):
        self.hasher = hasher

    def compare_with_directory(self, target_image, directory):
        target_hash = self.hasher.compute_phash(target_image)
        results = []

        for file in os.listdir(directory):
            path = os.path.join(directory, file)
            try:
                ref_hash = self.hasher.compute_phash(path)
                similarity = self.hasher.similarity(target_hash, ref_hash)
                results.append({
                    "image": file,
                    "similarity": similarity
                })
            except Exception:
                continue

        return results
