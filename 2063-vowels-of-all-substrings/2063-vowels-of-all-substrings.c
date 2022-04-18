
long long countVowels(char * word){
    long total = 0;
    int length = strlen(word);
    for(int i=0; i < length; i++){
        char ch = word[i];
        
        if (ch =='a' || ch =='e' || ch =='i'  || ch =='o'  || ch =='u') {
            total += (long)(i + 1) * (long)(length - i); 
        }
    }
    
    return total;
    
}

