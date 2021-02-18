package edu.lab3;

import javax.net.ssl.*;
import java.io.*;
import java.net.*;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.security.*;
import java.security.cert.CertificateException;
import java.security.cert.X509Certificate;

public class SSLClient {

    private static class SavingTrustManager implements X509TrustManager {

        private final X509TrustManager tm;
        protected X509Certificate[] chain;

        SavingTrustManager(X509TrustManager tm) {
            this.tm = tm;
        }

        public X509Certificate[] getAcceptedIssuers() {
            throw new UnsupportedOperationException();
        }

        public void checkClientTrusted(X509Certificate[] chain, String authType)
                throws CertificateException {
            throw new UnsupportedOperationException();
        }

        public void checkServerTrusted(X509Certificate[] chain, String authType)
                throws CertificateException {
            this.chain = chain;
            tm.checkServerTrusted(chain, authType);
        }
    }

    public static void getCertificate(String host, Integer port) throws IOException, NoSuchAlgorithmException, KeyManagementException, KeyStoreException, CertificateException{
        char[] password = "password".toCharArray();
        KeyStore ks = KeyStore.getInstance("JKS");
        FileInputStream fis = new FileInputStream("testkeyclientold.jks");
        ks.load(fis, password);

        SSLContext context = SSLContext.getInstance("TLS");
        TrustManagerFactory tmf =
                TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
        tmf.init(ks);
        X509TrustManager defaultTrustManager = (X509TrustManager)tmf.getTrustManagers()[0];
        SavingTrustManager tm = new SavingTrustManager(defaultTrustManager);
        context.init(null, new TrustManager[] {tm}, null);
        SSLSocketFactory factory = context.getSocketFactory();

        System.out.println("Opening connection to " + host + ":" + port + "...");
        SSLSocket socket = (SSLSocket)factory.createSocket(host, port);
        socket.setSoTimeout(10000);
        try {
            System.out.println("Starting SSL handshake...");
            socket.startHandshake();
            socket.close();
            System.out.println();
            System.out.println("No errors, certificate is already trusted");
        } catch (SSLException e) {
            System.out.println("Errors in SSL handshake");
        }

        X509Certificate[] chain = tm.chain;
        if (chain == null) {
            System.out.println("Could not obtain server certificate chain");
            return;
        }

        X509Certificate cert = chain[0];
        System.out.println("Version: "+cert.getVersion());
        System.out.println("Serial number: "+cert.getSerialNumber());
        System.out.println("Issuer: "+cert.getIssuerDN());
        System.out.println("Issue date: "+cert.getNotBefore());
        System.out.println("Expiration date: "+cert.getNotAfter());
        System.out.println("Subject: "+cert.getSubjectDN());
        System.out.println("Subject alternative names: "+cert.getSubjectAlternativeNames());
        System.out.println("Algorithm: "+cert.getSigAlgName());
        System.out.println("Public key: "+cert.getPublicKey());
        try {
            cert.verify(cert.getPublicKey());
        } catch (Exception e){
            System.out.println("WARNING: certificate is self signed!");
        }
    }

    public static void doGet(String host) throws IOException, InterruptedException {
        final HttpClient httpClient = HttpClient.newBuilder()
                .version(HttpClient.Version.HTTP_2)
                .build();

        HttpRequest request = HttpRequest.newBuilder()
                .GET()
                .uri(URI.create(host))
                .setHeader("User-Agent", "Java 11 HttpClient Bot")
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        writeHtmlFile(response.body());
    }

    public static void writeHtmlFile(String body){
        try {
            FileWriter myWriter = new FileWriter("body.txt");
            myWriter.write(body);
            myWriter.close();
            System.out.println("Successfully wrote html file.");
        } catch (IOException e) {
            System.out.println("Exception writing html file");
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        Integer port = 443;
        try {
            //doGet("https://bnr.ro/Home.aspx");
            getCertificate("www.bnr.ro", port);
            //getCertificate("127.0.0.1",8000);
        } catch (IOException e) {
            System.out.println("IOException in getCertificate!");
            e.printStackTrace();
        } catch (NoSuchAlgorithmException e){
            System.out.println("Wrong algorithm!");
        } catch (KeyManagementException e){
            System.out.println("Key management exception!");
        } catch (KeyStoreException e){
            System.out.println("Keystore exception!");
        } catch (CertificateException e){
            System.out.println("Certificate exception!");
        } catch (Exception e) {
            System.out.println("Other exception!");
        }

    }


}



