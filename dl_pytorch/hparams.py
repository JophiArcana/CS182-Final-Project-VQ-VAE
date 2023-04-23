from argparse import Namespace

HP = Namespace(
    batch_size=32,
    lr=1e-3,
    momentum=0.9,
    lr_decay=0.99,
    optim_type="adam",
    l2_reg=0.0,
    epochs=10,
    hidden_channels=128,
    num_residual_layers=2,
    residual_hidden_channels=32,
    num_embeddings=512,
    embedding_dim=64
)
