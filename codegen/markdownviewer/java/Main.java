/*
Requires https://github.com/atlassian/commonmark-java

    <dependency>
        <groupId>com.atlassian.commonmark</groupId>
        <artifactId>commonmark</artifactId>
        <version>0.13.1</version>
    </dependency>

*/
package dev.deskriders.devrider.markdown;

import org.commonmark.node.Node;
import org.commonmark.parser.Parser;
import org.commonmark.renderer.html.HtmlRenderer;

public class MarkdownViewer {
    public static String convertToHtml(String source) {
        Parser mdParser = Parser.builder().build();
        Node parsedNode = mdParser.parse(source);
        HtmlRenderer htmlRenderer = HtmlRenderer.builder().build();
        return htmlRenderer.render(parsedNode);
    }
}
