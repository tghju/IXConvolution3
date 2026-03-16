import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# ============================================================
# CNN KERNEL LAB
#
# Goal:
# Build a tiny feature extractor for classifying circles vs squares.
#
# For each image, your program should:
#   1. apply several kernels
#   2. apply ReLU
#   3. apply max pooling
#   4. turn each pooled feature map into one score
#   5. use those scores to predict the class
# ============================================================


# ============================================================
# SECTION 1: SETTINGS
#
# These folder names should match your project structure.
# ============================================================

CLASS_A_FOLDER = "data/circles"
CLASS_B_FOLDER = "data/squares"
IMAGE_SIZE = (128, 128)


# ============================================================
# SECTION 2: LOAD IMAGES
#
# This helper function is already written for you.
# It loads every image in a folder, resizes it, and scales
# pixel values to be between 0 and 1.
# ============================================================

def load_images(folder, size):
    images = []
    filenames = []

    for filename in sorted(os.listdir(folder)):
        path = os.path.join(folder, filename)

        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue

        img = cv2.resize(img, size)
        img = img.astype(np.float32) / 255.0

        images.append(img)
        filenames.append(filename)

    return images, filenames


# ============================================================
# SECTION 3: RELU
#
# ReLU replaces all negative values with 0.
# ============================================================

def relu(x):
    return np.maximum(x, 0)


# ============================================================
# SECTION 4: MAX POOLING
#
# This function breaks an image into non-overlapping blocks
# and keeps only the largest number from each block.
# ============================================================

def max_pool(img, size=2):
    h, w = img.shape
    h2 = h - (h % size)
    w2 = w - (w % size)
    img = img[:h2, :w2]

    return img.reshape(h2 // size, size, w2 // size, size).max(axis=(1, 3))


# ============================================================
# SECTION 5: STUDENT KERNELS
#
# TASK:
# Create THREE different 3x3 kernels.
#
# Suggestions:
#   - one edge detector
#   - one corner detector
#   - one custom kernel
#
# Then store them in a list called kernels.
# ============================================================

# Example:
# kernel1 = np.array([
#     [ 1, 0, -1],
#     [ 1, 0, -1],
#     [ 1, 0, -1]
# ], dtype=np.float32)

# TODO: define kernel1
# TODO: define kernel2
# TODO: define kernel3

kernels = []


# ============================================================
# SECTION 6: APPLY ONE KERNEL TO ONE IMAGE
#
# TASK:
# Complete this function.
#
# It should:
#   1. apply the kernel with cv2.filter2D
#   2. apply ReLU
#   3. apply max pooling
#   4. compute a score using np.max on the pooled map
#
# Return:
#   feature_map, pooled_map, score
# ============================================================

def process_image(image, kernel):

    # Step 1: apply the kernel to the image
    feature_map = cv2.filter2D(image, -1, kernel)

    # Step 2: apply ReLU to the feature map
    feature_map = relu(feature_map)

    # Step 3: apply max pooling
    pooled_map = None   # TODO: replace None

    # Step 4: compute the score from the pooled map
    score = None        # TODO: replace None

    return feature_map, pooled_map, score


# ============================================================
# SECTION 7: EXTRACT FEATURES FROM ONE IMAGE
#
# TASK:
# Apply every kernel in the list to one image.
# Save the score from each kernel into a list called features.
#
# Example output:
#   [2.1, 0.8, 1.7]
# ============================================================

def extract_features(image, kernels):
    features = []

    for kernel in kernels:
        # Use process_image to get the score for this kernel
        feature_map, pooled_map, score = None, None, None   # TODO

        # Find various ways to score the pooled map, such as:
        #   - np.max(pooled_map)    
        #   - np.mean(pooled_map)
        #   - np.sum(pooled_map)
        # Add the score to the features list
        # TODO

    # After this loop, features should be a list of scores, several for each kernel.
    return features


# ============================================================
# SECTION 8: MAKE A PREDICTION
#
# TASK:
# Write a simple rule that predicts:
#   0 for circles
#   1 for squares
#
# based on the feature scores.
#
# Start simple. For example:
#   compare one feature to another
#   or combine two features
# ============================================================

def predict_class(features):

    # Example:
    # feature0 = features[0]
    # feature1 = features[1]

    prediction = None   # TODO: replace None
    return prediction


# ============================================================
# SECTION 9: EVALUATE MANY IMAGES
#
# TASK:
# For every image:
#   1. extract its features
#   2. predict its class
#   3. compare prediction to the true label
#
# Then compute:
#   accuracy = correct / total
# ============================================================

def evaluate_dataset(images, kernels, true_label):
    correct = 0
    total = len(images)

    for image in images:
        # Step 1: get the feature vector for this image
        features = None   # TODO

        # Step 2: predict the class
        prediction = None   # TODO

        # Step 3: count correct predictions
        if prediction == true_label:
            correct += 1

    accuracy = None   # TODO
    return accuracy


# ============================================================
# SECTION 10: VISUALIZE RESULTS
#
# This helper function is already written for you.
# It shows:
#   - the original image
#   - the feature map
#   - the pooled map
# ============================================================

def show_results(image, feature_map, pooled_map, title=""):
    fig, axes = plt.subplots(1, 3, figsize=(10, 4))

    axes[0].imshow(image, cmap="gray")
    axes[0].set_title("Original")
    axes[0].axis("off")

    axes[1].imshow(feature_map, cmap="gray")
    axes[1].set_title("Feature Map")
    axes[1].axis("off")

    axes[2].imshow(pooled_map, cmap="gray")
    axes[2].set_title("Pooled Map")
    axes[2].axis("off")

    plt.suptitle(title)
    plt.tight_layout()
    plt.show()


# ============================================================
# SECTION 11: MAIN PROGRAM
#
# TASK:
# Complete the main function so that it:
#   1. loads circle images
#   2. loads square images
#   3. prints one example feature vector for a circle
#   4. prints one example feature vector for a square
#   5. evaluates accuracy on circles
#   6. evaluates accuracy on squares
#   7. prints overall accuracy
#   8. shows one example visualization
# ============================================================

def main():
    circle_images, circle_names = load_images(CLASS_A_FOLDER, IMAGE_SIZE)
    square_images, square_names = load_images(CLASS_B_FOLDER, IMAGE_SIZE)

    if not circle_images or not square_images:
        print("Could not find images.")
        print("Make sure your folders look like this:")
        print("data/circles")
        print("data/squares")
        return

    # Print one example feature vector from each class
    # Use the first image in each list
    circle_features = None   # TODO
    square_features = None   # TODO

    print("Example circle feature vector:", circle_features)
    print("Example square feature vector:", square_features)

    # Evaluate each class separately
    circle_accuracy = None   # TODO
    square_accuracy = None   # TODO

    # Compute weighted overall accuracy
    total_images = len(circle_images) + len(square_images)
    overall_accuracy = None   # TODO

    print("Circle accuracy:", circle_accuracy)
    print("Square accuracy:", square_accuracy)
    print("Overall accuracy:", overall_accuracy)

    # Show one example visualization
    # Choose one image and one kernel
    example_image = circle_images[0]
    example_kernel = kernels[0]

    feature_map, pooled_map, score = None, None, None   # TODO

    show_results(
        example_image,
        feature_map,
        pooled_map,
        title=f"Example score = {score}"
    )


if __name__ == "__main__":
    main()