from abc import ABC, abstractmethod
from typing import List

class AbstractMetadataRemover(ABC):
    """Abstract base class for metadata removal."""

    @abstractmethod
    def remove_metadata(self, image_path: str, output_path: str) -> None:
        """Remove specified metadata from the image."""
        pass

    @abstractmethod
    def get_metadata_fields(self) -> List[str]:
        """Return the list of metadata fields to be removed."""
        pass
