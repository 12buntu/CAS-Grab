from blabel import LabelWriter
from resourcemanage import Resource_Manager
import json
from pathlib import Path

current_dir = Path(__file__).parent


class LabelGenerator:
    def __init__(self):
        self.label_writer = LabelWriter(
            str(current_dir / "label.html"),
            default_stylesheets=(str(current_dir / "style.css")),
        )
        self.records = []
        self.rm = Resource_Manager()
        self.path = self.rm.printer_path

    def add_item(self, id: int):
        item: dict = self.rm.get_item(id)
        ## adds records to list to be printed
        self.records.append(
            dict(
                id_num=id,
                name=item["title"],
                received_date = json.loads(item["metadata"]["extra_fields"]).to_dict()["Received Date"]["value"]
                qr_json=json.dumps({"id": id}),
            )
        )

    # generates pdf for all labels in records
    def write_labels(self):
        self.label_writer.write_labels(self.records, target=self.path)
        self.records = []
