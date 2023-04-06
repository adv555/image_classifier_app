# IMAGE CLASSIFIER WEB APP


This web application provides classification service for any image to 10 different classes such as airplanes, cars, birds, cats, deer, dogs, frogs, horses, ships, and trucks using CNN model trained with [CIFAR-10](https://www.kaggle.com/c/cifar-10).

### Model
The model is created using [Xception](https://keras.io/api/applications/xception/) convolutional base and can be changed to users model via website form.

[//]: # (Such methods as data augmentation, DropBlock2D, GlobalAveragePooling2D, Dropblock, ReduceLROnPlateau are used to prevent an overfitting of the model.)
The model's test accuracy score is 97.16% on [CIFAR-10](https://www.kaggle.com/c/cifar-10) test dataset.

**_Tech used_**

- [Django](https://platform.openai.com/)
- [Keras](https://keras.io/)
- [Tailwindcss](https://tailwindcss.com)
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/)
- [Cloudinary](https://cloudinary.com/)
- [Docker](https://www.docker.com/)

### Installation
1. You need to have pre installed IDE and Docker
2. Create new project and clone project from git in your IDE
3. Copy .env.example to .env:<br />
4. Build containers via `docker-compose`:

   ```bash
   docker-compose build
   ```

5. Start containers:

   ```bash
   docker-compose up
   ```

6. Open `http://localhost:8000` in a browser. You should see the main page.
