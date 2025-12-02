#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>

char *read_file(const char *file_name) {
    FILE *fptr = fopen(file_name, "rb");
    assert(fptr != NULL);
    
    assert(fseek(fptr, 0L, SEEK_END) == 0);
    long file_size = ftell(fptr);
    assert(file_size != -1L);
    rewind(fptr);
    
    char *file_contents = (char *)malloc(sizeof(char)*(file_size+1));
    
    const size_t bytes_read = fread(file_contents, sizeof(char), file_size, fptr);
    assert(bytes_read == file_size);
    
    file_contents[file_size] = '\0';
    fclose(fptr);
    
    return file_contents;
}

char **split(char *

int main() {
    char *contents = read_file("input.txt");
    printf("%s", contents);
    free(contents);
    return 0;
}


