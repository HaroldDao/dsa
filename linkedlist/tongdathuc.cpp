#include <iostream>

using namespace std;

struct ele {
    int heso, somu;
    ele *next = NULL;  
    ele (int hs, int sm) {
        heso = hs;
        somu = sm;
    }  
};

struct poly { // poly: polynomials
    ele *first = NULL;

    void defineP(ele *val) { // polynomial difine
        if (val == NULL) return;

        val->next = NULL;
        if (first == NULL) {
            first = val;
            return;
        }
        ele *curr = first;
        while (curr->next != NULL) {
            curr = curr->next;
        }
        curr->next = val;
    }

    void showP() {
        if (first == NULL) return;

        ele *curr = first;
        int plusCheck = 0;
        while (curr != NULL) {
            if (curr->next != NULL) plusCheck = 1;
            if (curr->somu < 2) {
                if (curr->somu == 1) cout << curr->heso << "x"; 
                else if (curr->somu == 0) {
                    cout << curr->heso;
                }
            } else {
                cout << curr->heso << "x^" << curr->somu;
            }
            if (plusCheck == 1) cout << " + ";
            plusCheck = 0;
            curr = curr->next; 
        }
    }
};

void sumP(poly *x, poly *y, poly *res) {
    if (x == NULL || y == NULL) return;

    ele *a = x->first, *b = y->first;
    while (a != NULL && b != NULL) {
        if (a->somu == b->somu) {
            if (a->heso + b->heso != 0)
                res->defineP(new ele((a->heso + b->heso), a->somu));
            a = a->next;
            b = b->next;
        } else if (a->somu > b->somu) {
            res->defineP(new ele(a->heso, a->somu));
            a = a->next;
        } else {
            res->defineP(new ele(b->heso, b->somu));
            b = b->next;
        }
    }

    if (a != NULL) {
        while (a != NULL) {
            res->defineP(new ele(a->heso, a->somu));
            a = a->next;
        }
    } else if (b != NULL) {        
        while (b != NULL) {
            res->defineP(new ele(b->heso, b->somu));
            b = b->next;
        }
    }
} 

int main() {
    poly *A = new poly, *B = new poly, *Tong = new poly;

    // polynomial A define A(x) = 4x^10 -2x^3 + 5x^2 + 7
    A->defineP(new ele(4, 10));
    A->defineP(new ele(-2, 3));
    A->defineP(new ele(5, 2));
    A->defineP(new ele(7, 0));

    // polynomial B define B(x) = -6x^10 + 8x^6 + 2x^3 + 1
    B->defineP(new ele(-6, 10));
    B->defineP(new ele(8, 6));
    B->defineP(new ele(2, 3));
    B->defineP(new ele(1, 0));
    
    // Idea: we use for loop to define a polynomial expression instead of hard defination.

    sumP(A, B, Tong);

    Tong->showP();
}
