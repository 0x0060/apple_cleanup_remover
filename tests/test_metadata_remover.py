import unittest
import os
from apple_cleanup_remover.metadata_remover import MetadataRemover

class TestMetadataRemover(unittest.TestCase):

    def setUp(self) -> None:
        self.remover = MetadataRemover()
        self.test_image_path = 'test_image.jpg'
        self.output_image_path = 'output_test_image.jpg'

    def test_remove_metadata(self) -> None:
        """Test the removal of metadata."""
        self.remover.remove_metadata(self.test_image_path, self.output_image_path)
        self.assertTrue(os.path.exists(self.output_image_path))

    def tearDown(self) -> None:
        """Clean up output files after tests."""
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

if __name__ == '__main__':
    unittest.main()
