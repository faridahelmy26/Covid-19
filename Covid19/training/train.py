from app.model.train_model import build_model
from training.dataset_loader import get_data_generators

train_dir = "data/train"
test_dir = "data/test"

train_generator, test_generator = get_data_generators(train_dir, test_dir)

model = build_model()

history = model.fit(
    train_generator,
    validation_data=test_generator,
    epochs=5
)

model.save("app\model\model.h5")