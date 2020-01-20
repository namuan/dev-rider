package dev.deskriders.devrider.codecs;

import java.util.Base64;

public class Base64EncoderDecoder {
    public static String encode(String source) {
        return Base64.getEncoder().encodeToString(source.getBytes());
    }

    public static String decode(String source) {
        return new String(Base64.getDecoder().decode(source));
    }
}
