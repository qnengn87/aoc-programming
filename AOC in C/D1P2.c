#include <stdio.h>
#include <stdlib.h>
#include <assert.h>


char *read_file(const char *file_name) {
    int buffer_size = 10000*sizeof(char);
    char *buffer = (char *)malloc(buffer_size);

    FILE *fptr = fopen(file_name, "r");
    
    assert(fptr != NULL);
    
    while (fgets(buffer, buffer_size, fptr) != NULL) {}
    fclose(fptr);
    return buffer;
}

int solve(const char *contents) {
    int count=0;
    int position=0;
    
    int i=0;
    char curr = contents[i];
    while (curr != '\0' && position == 0) {
        assert(curr == '(' || curr == ')' || curr == '\n');
        if (curr == '(') {
            count++;
        } 
        if (curr == ')') {
            count--;
        }
        if (count == -1) {
            position = i;
        }
        i++;
        curr = contents[i];
    }
    
    return position+1; 
}

int main() {
    char *contents = read_file("input.txt");
    int solution = solve(contents);
    
    free(contents);
    
    printf("%d\n", solution);
    return solution;
}


