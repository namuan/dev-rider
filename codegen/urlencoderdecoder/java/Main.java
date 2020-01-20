/*
Requires Apache commons-codec - https://mvnrepository.com/artifact/commons-codec/commons-codec

    <dependency>
        <groupId>commons-codec</groupId>
        <artifactId>commons-codec</artifactId>
        <version>1.13</version>
    </dependency>
*/
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.net.URLCodec;

public class UrlEncoderDecoder {
    public static String encode(String source) throws EncoderException {
        return new URLCodec().encode(source);
    }

    public static String decode(String source) throws DecoderException {
        return new URLCodec().decode(source);
    }
}
