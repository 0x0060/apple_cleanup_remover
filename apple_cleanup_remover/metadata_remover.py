from PIL import Image
import piexif
from typing import List
from .abc_metadata_remover import AbstractMetadataRemover

class MetadataRemover(AbstractMetadataRemover):
    """Class to remove specified metadata from images."""

    def __init__(self) -> None:
        self.metadata_fields_to_remove: List[str] = [
            "CurrentlPTCDigest",
            "CodedCharacterSet",
            "ApplicationRecordVersion",
            "DigitalCreationTime",
            "DigitalCreationDate",
            "Credit",
            "DateCreated",
            "TimeCreated",
            "IPTCDigest",
            "XMPT001kit",
            "CreatorTool",
            "DigitalSourceType",
            "DateTimeCreated",
            "DigitalCreationDateTime"
        ]

    def remove_metadata(self, image_path: str, output_path: str) -> None:
        """Remove specified metadata from an image and save it."""
        img = Image.open(image_path)
        exif_dict = piexif.load(img.info.get("exif", b""))

        for field in self.metadata_fields_to_remove:
            for ifd in exif_dict:
                if field in exif_dict[ifd]:
                    del exif_dict[ifd][field]

        exif_bytes = piexif.dump(exif_dict)

        img.save(output_path, exif=exif_bytes)

    def get_metadata_fields(self) -> List[str]:
        """Return the list of metadata fields to be removed."""
        return self.metadata_fields_to_remove
