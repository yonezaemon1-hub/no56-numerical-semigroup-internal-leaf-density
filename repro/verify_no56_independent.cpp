// No.56 independent C++17 verifier: bitset sumset + incremental count.
// Tested on Linux x86_64 by the creation side. No Windows-run claim.
#include <cstdint>
#include <cstdio>
#include <cassert>
using namespace std;
uint64_t count_leaves(int m){
  const uint64_t need = ((1ULL<<m)-1ULL)<<4;
  uint64_t total=0;
  for(int a=0;a<3;a++){
    const uint64_t a12=a==1 ? (1ULL<<1) : (a==2 ? (1ULL<<2) : 0ULL);
    for(int b=0;b<4;b++){
      if(a==1 && b!=3) continue;
      if(a==2 && !(b&2)) continue;
      const uint64_t base=1ULL|a12|(1ULL<<m)|
                       ((b&1)?(1ULL<<(m+1)):0ULL)|
                       ((b&2)?(1ULL<<(m+2)):0ULL);
      for(uint64_t free=0;free<(1ULL<<(m-4));free++){
        uint64_t x=base|(free<<4),sumset=0,remaining=x;
        while(remaining){
          int i=__builtin_ctzll(remaining);
          sumset|=x<<i;
          remaining&=remaining-1;
        }
        total+=((sumset&need)==need);
      }
    }
  }
  return total;
}
const int LIMIT=32;
uint64_t qcounts[LIMIT+1]={0};
void visit(int k,uint64_t mask,unsigned weight){
  qcounts[k-1]+=weight;
  if(k>LIMIT)return;
  visit(k+1,mask|(1ULL<<(k-1)),weight);
  for(int i=1;i<=k/2;i++){
    int j=k-i;
    if(((mask>>(i-1))&1ULL)&&((mask>>(j-1))&1ULL)){
      visit(k+1,mask,weight);
      break;
    }
  }
}
int main(){
  const uint64_t leaves[]={7,13,19,41,73,152,284,578,1104,2245,4344,
        8770,17119,34495,67812,136264,269175,540254,1071144};
  for(int m=6;m<=24;m++){
    uint64_t got=count_leaves(m);
    assert(got==leaves[m-6]);
    printf("PASS m=%d N=%llu L=%llu\n",m,
        (unsigned long long)(7ULL<<(m-4)),(unsigned long long)got);
  }
  visit(4,0ULL,4);visit(4,1ULL,1);visit(4,2ULL,2);
  assert(qcounts[6]==13);
  assert(qcounts[12]==596);
  assert(qcounts[18]==34870);
  assert(qcounts[22]==543345);
  assert(qcounts[25]==4294283);
  assert(qcounts[32]==543583947);
  printf("PASS Q32=%llu/3758096384\n",(unsigned long long)qcounts[32]);
  return 0;
}
