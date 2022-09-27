import matplotlib.pyplot as plt

def show_chart() :
    plt.plot([9,9.2,9.6,7.5,6.7,7],[9.4,9.2,9.2,9.2,7.1,7.4],'yx')
    plt.plot([9,9.2,9.5,7.5,5.7,7],[9.4,9.2,9.2,9.2,7.1,7.4],'yx')

    plt.plot([7.2,7.3,7.2,7.3,7.2,7.3,7.3],[18.3,10.5,9.2,10.2,9.7,18.1,18.1],'gx')
    plt.plot([6.5,9.0],[7.8,12.5],'b--')

    plt.ylabel("H cm")
    plt.xlabel("W cm")

    plt.legend(('Orange','Lemons'),loc='upper right')
    plt.show()

def main() :
    show_chart()

if __name__ == "__main__" :
    main()
