package org.apache.lucene.search.similarities;
import org.apache.lucene.index.FieldInvertState;
import org.apache.lucene.search.similarities.ClassicSimilarity;;

public class ModVSM extends ClassicSimilarity {

@Override
public float coord(int overlap, int maxOverlap) {
    return super.coord(overlap, maxOverlap);
}

@Override
public float idf(long docFreq, long numDocs) {
    return super.idf(docFreq, numDocs);
}

@Override
public float lengthNorm(FieldInvertState arg0) {
    return super.lengthNorm(arg0);
}

@Override
public float tf(float freq) {
    return 1.5f*super.tf(freq);
}

}