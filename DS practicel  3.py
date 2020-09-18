#P3. Implement the following for stack.
 A) Perform stack operations using array implementation
        
  Code:
stack = [] 

stack.append('a') 

stack.append('b') 

stack.append('c') 

  

print('Initial stack') 

print(stack)

print('\nElements poped from stack:') 

print(stack.pop()) 

print(stack.pop()) 

print(stack.pop()) 

  

print('\nStack after elements are poped:') 

print(stack) 

B) Implement tower of hanoi

Code:
def TowerOfHanoi(n , source, destination, auxiliary): 

    if n==1: 

        print "Move disk 1 from source",source,"to destination",destination 

        return

    TowerOfHanoi(n-1, source, auxiliary, destination) 

    print "Move disk",n,"from source",source,"to destination",destination 

    TowerOfHanoi(n-1, auxiliary, destination, source) 

          
# Driver code 

n = 4

TowerOfHanoi(n,'A','B','C')  

C) wap to scan a polyano mail using linked list
and add two polynomial
struct Node 

{ 

    int coeff; 

    int pow; 

    struct Node *next; 

};               

// Function to create new node 

void create_node(int x, int y, struct Node **temp) 

{ 

    struct Node *r, *z; 

    z = *temp; 

    if(z == NULL) 

    { 

        r =(struct Node*)malloc(sizeof(struct Node)); 

        r->coeff = x; 

        r->pow = y; 

        *temp = r; 

        r->next = (struct Node*)malloc(sizeof(struct Node)); 

        r = r->next; 

        r->next = NULL; 

    } 

    else

    { 

        r->coeff = x; 

        r->pow = y; 

        r->next = (struct Node*)malloc(sizeof(struct Node)); 

        r = r->next; 

        r->next = NULL; 

    } 

}   

// Function Adding two polynomial numbers 

void polyadd(struct Node *poly1, struct Node *poly2, struct Node *poly) 

{ 

while(poly1->next && poly2->next) 

    { 

        // If power of 1st polynomial is greater then 2nd, then store 1st as it is 

        // and move its pointer 

        if(poly1->pow > poly2->pow) 

        { 

            poly->pow = poly1->pow; 

            poly->coeff = poly1->coeff; 

            poly1 = poly1->next; 

        }   

        // If power of 2nd polynomial is greater then 1st, then store 2nd as it is 

        // and move its pointer 

        else if(poly1->pow < poly2->pow) 

        { 

            poly->pow = poly2->pow; 

            poly->coeff = poly2->coeff; 

            poly2 = poly2->next; 

        } 

          // If power of both polynomial numbers is same then add their coefficients 

        else

        { 

            poly->pow = poly1->pow; 

            poly->coeff = poly1->coeff+poly2->coeff; 

            poly1 = poly1->next; 

            poly2 = poly2->next; 

        }    

        // Dynamically create new node 

        poly->next = (struct Node *)malloc(sizeof(struct Node)); 

        poly = poly->next; 

        poly->next = NULL; 

    } 

while(poly1->next || poly2->next) 

    { 

        if(poly1->next) 

        { 

            poly->pow = poly1->pow; 

            poly->coeff = poly1->coeff; 

            poly1 = poly1->next; 

        } 

        if(poly2->next) 

        { 

            poly->pow = poly2->pow; 

            poly->coeff = poly2->coeff; 

            poly2 = poly2->next; 

        } 

        poly->next = (struct Node *)malloc(sizeof(struct Node)); 

        poly = poly->next; 

        poly->next = NULL; 

    } 

}  

// Display Linked list 

void show(struct Node *node) 

{ 

while(node->next != NULL) 

    { 

    printf("%dx^%d", node->coeff, node->pow); 

    node = node->next; 

    if(node->next != NULL) 

        printf(" + "); 

    } 

}  

int main() 

{ 

    struct Node *poly1 = NULL, *poly2 = NULL, *poly = NULL;    

    // Create first list of 5x^2 + 4x^1 + 2x^0 

    create_node(5,2,&poly1); 

    create_node(4,1,&poly1); 

    create_node(2,0,&poly1);   

    // Create second list of 5x^1 + 5x^0 

    create_node(5,1,&poly2); 

    create_node(5,0,&poly2);   

    printf("1st Number: ");  

    show(poly1); 

    printf("\n2nd Number: "); 

    show(poly2);     

    poly = (struct Node *)malloc(sizeof(struct Node));      

    // Function add two polynomial numbers 

    polyadd(poly1, poly2, poly);    

    // Display resultant List 

    printf("\nAdded polynomial: "); 

    show(poly);   

return 0; 

}  


D)wap to calculate factorial and to complete the
Factors of give no using recursion and using iteration

# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num)) un









