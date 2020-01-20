import java.util.Base64;

class Main {

    public String encode(String src) {
        return Base64.getEncoder().encodeToString(src.getBytes());
    }

    public String decode(String src) {
        return new String(Base64.getDecoder().decode(src));
    }

}