from plotter import plot_basic_scales, plot_supplementary_scales 


def main():
    
    scores_page1 = [ 45, 33, 30, 65, 44, 89, 54, 65, 76, 45, 89, 92, 34 ]

    k_score = 30

    gender = "Female"

    plot_basic_scales(scores_page1, k_score, gender)

    scores_page2 = [56, 76, 56, 89, 37, 47, 98, 56, 88, 90, 94, 65, 73, 78, 89, 30, 43, 43, 68 ]

    plot_supplementary_scales(scores_page2, gender)

if __name__ == "__main__":
    main()
