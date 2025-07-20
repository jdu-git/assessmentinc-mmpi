from plotter import basic_scales
from plotter import supplementary_scales


def main():
    
    scores_page1 = [ 45, 54, 23, 15, 76, 89, 54, 65, 76, 45, 89, 104, 34 ]

    k_score = 23

    gender = "Female"

    basic_scales(scores_page1, k_score, gender)

    scores_page2 = [ 45, 56, 76, 56, 89, 27, 47, 98, 56, 88, 90, 94, 65, 73, 78, 89, 20, 43, 43, 68 ]

    supplementary_scales(scores_page2, gender)

if __name__ == "__main__":
    main()
