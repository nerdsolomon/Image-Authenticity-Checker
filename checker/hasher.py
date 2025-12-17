from PIL import Image
import imagehash


class ImageHasher:
    def __init__(self, hash_size=8):
        self.hash_size = hash_size

    def compute_phash(self, image_path):
        img = Image.open(image_path).convert("RGB")
        return imagehash.phash(img, hash_size=self.hash_size)

    @staticmethod
    def similarity(hash1, hash2):
        max_dist = hash1.hash.size
        dist = hash1 - hash2
        return round((1 - dist / max_dist) * 100, 2)
