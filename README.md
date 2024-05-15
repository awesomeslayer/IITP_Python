# Fast Hough Transform

Fast Hough Transform is a Python package that provides efficient algorithms for performing Hough transform for line detection in images. It demonstrates the usage of Poetry for dependency management, Nox for task automation, continuous integration and continuous deployment (CI/CD) pipelines, and includes comprehensive test coverage.

## Features

- Efficient implementation of Hough transform for line detection in images.
- Utilizes Poetry for dependency management.
- Task automation with Nox.
- Continuous integration and continuous deployment (CI/CD) pipelines.
- Comprehensive test suite for ensuring code quality and reliability.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/fast-hough-transform.git
2. Navigate to the project directory:
   ```bash
   cd fast-hough-transform
3. Install dependencies using Poetry:
   ``bash
   poetry install
## Usage

To perform a fast Hough transform on an image and detect lines, you can use the provided functions in the `fast_hough_transform` package. Here's a basic example:

```python
import cv2
from fast_hough_transform.hough_transform import hough_transform
from fast_hough_transform.image_processing import read_image

# Read an image
image = read_image("path/to/image.png")

# Perform Hough transform
accumulator, thetas, rhos = hough_transform(image)

# Display the results
# (Add your code here to visualize the results)
```
## Testing

To run the test suite, execute the following command:

```bash
nox -rs tests
```
This command will run the tests using the specified Nox session (tests) and display the results, including code coverage.

## Linting

To lint the code using Nox, execute the following command:

```bash
nox -rs lint
```
This command will run the linting tasks defined in the Noxfile and ensure code style consistency.

##Documentation

This command will run the generation of documentation in HTML in _build directory.

```bash
nox -rs docs
```

##You can see more nox session in noxfile.py
