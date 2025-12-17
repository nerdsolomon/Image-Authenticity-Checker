from PIL import Image, ExifTags


class ExifReader:
    RELEVANT_FIELDS = {
        "DateTimeOriginal": "Date Taken",
        "Model": "Device Model",
        "Orientation": "Orientation",
        "GPSInfo": "Geolocation",
        "DateTime": "Modification Date"
    }

    def extract(self, image_path):
        try:
            img = Image.open(image_path)
            raw_exif = img._getexif()
            if not raw_exif:
                return None

            exif = {}
            for tag, value in raw_exif.items():
                decoded = ExifTags.TAGS.get(tag, tag)
                if decoded in self.RELEVANT_FIELDS:
                    exif[self.RELEVANT_FIELDS[decoded]] = value

            return exif if exif else None
        except Exception:
            return None
