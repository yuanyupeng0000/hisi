#include <unistd.h>
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string>

#include "opencv2/opencv.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

using namespace cv;

typedef unsigned char U_CHAR;

int main(int argc, char* argv[]) 
{
        if(argc != 5) 
        {
            fprintf(stderr, "Usage:%s [src_file] [out_file] [dst_width] [dst_height]\n", argv[0]);
            exit(-1);
        }
	const char *filename = argv[1];
	const char *outname = argv[2];
        unsigned int u32width = atoi(argv[3]);
        unsigned int u32height = atoi(argv[4]);

	cv::Mat img = cv::imread(filename);
	if (!img.data)
	{
		printf("read image error\n");
		return -1;
	}

	//缩放
	resize(img, img, Size(u32width, u32height));  //224x224
	//imshow("img",img);
	//waitKey(0);

	U_CHAR *data = (U_CHAR*)img.data;
	int step = img.step;
	printf("Step: %d, height: %d, width: %d\n",
		step, img.rows, img.cols);

	FILE *fp = fopen(outname, "wb");
	int h = img.rows;
	int w = img.cols;
	int c = img.channels();

	for (int k = 0; k<c; k++) {
		for (int i = 0; i<h; i++) {
			for (int j = 0; j<w; j++) {
				fwrite(&data[i*step + j*c + k], sizeof(U_CHAR), 1, fp);
			}
		}
	}
	fclose(fp);

	return 0;
}

