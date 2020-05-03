import setuptools

with open("Readme.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="predict", # Replace with your own username
    version="0.0.1",
    author="Aarti",
    author_email="aartitayade96@gmail.com",
    description="Prediction of bike rental count on the basis of different weather situation",
    long_description=long_description,
    long_description_content_type="text/text",
    url="https://github.com/pypa/sampleproject",
    #packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
	py_modules= ['day2'],
	install_requires=['pandas','matplotlib','sklearn','numpy','pytest',],
	entry_points={
        'console_scripts': [
            'predict=src.day2:predict_cnt',
			'plot=src.day2:plot',
			
        ],
    }
	
)