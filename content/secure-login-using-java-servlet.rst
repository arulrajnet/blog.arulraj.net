Secure login using java servlet
###############################
:date: 2009-07-25 04:57
:author: arul
:category: Programming
:tags: java
:slug: secure-login-using-java-servlet

The user authentication is the common task when we create a web
application. The servlet have j\_security\_check  authentication method.
This is commonly called as **form based authentication.** Here the steps
for this authentication.

|image0|

| This is in your index.jsp or login page
| 
  `` <form action="j_security_check" method="post"> Username <input name="j_username" type="text" /> Password <input name="j_password" type="password" /> <input type="submit" value="Login" /> </form>``

Add below code in your web.xml

::

    <login-config>
            <auth-method>FORM</auth-method>
            <realm-name>Real Name</realm-name>
            <form-login-config>
                <form-login-page>LoginPage.jsp</form-login-page>
                <form-error-page>LoginPageError.jsp</form-error-page>
                </form-login-config>
    </login-config>

     <security-role>
     <description>view all permissions</description>
     <role-name>admin</role-name>
     </security-role>

     <security-role>
     <description>limited permissions</description>
     <role-name>user</role-name>
     </security-role>

     <resource-ref>
     <description>jdbc:mysql://localhost:3306/databasename</description>
     <res-ref-name>mysql/pooldb</res-ref-name>
     <res-type>javax.sql.DataSource</res-type>
     <res-auth>Container</res-auth>
     <res-sharing-scope>Shareable</res-sharing-scope>
     </resource-ref>

Add below code in your Tomcat's \\conf\\server.xml

::

    <Realm className="org.apache.catalina.realm.JDBCRealm" debug="99"
        driverName="com.mysql.jdbc.Driver"
        connectionURL="jdbc:mysql://localhost/DBNAME?user=DBUSER&amp;password=DBPASS"
        userTable="USERTABLE" userNameCol="NAMECOLUMN" userCredCol="PASSCOLUMN"
        userRoleTable="ROLETABLE" roleNameCol="ROLECOLUMN"/>

For this you need two tables in your database. One is username table
that contains username and password column. And another one is userrole
table that contains username and role column.

-  **debug** —Here, we set the debug level. A higher number generates
   more detailed output.
-  **driverName** —The name of our MySQL driver. You need to be sure
   that the driver's JAR file is located in Tomcat's CLASSPATH.
-  **connectionURL** —The database URL that is used to establish a JDBC
   connection. In this field, weblogin is the name of our database; user
   and password are login data with which you are connecting to the
   database. In MySQL, such a user is created by default, so you can use
   it. In case you don't have such a user, you need to create your own
   user and make it capable of working with your weblogin database.
-  **userTable** —A table with at least two fields, defined in
   userNameCol and userCredCol.
-  **userNameCol** and userCredCol—The fields with the name of login
   field from the users table and pass.

For more info `Realm How
to <http://tomcat.apache.org/tomcat-5.5-doc/realm-howto.html>`__ ...

.. |image0| image:: http://2.bp.blogspot.com/_Tq9uaJI0Xww/SmriIO1lnLI/AAAAAAAAFJM/6ru3Sprujzs/s400/tomcat.png
   :target: http://2.bp.blogspot.com/_Tq9uaJI0Xww/SmriIO1lnLI/AAAAAAAAFJM/6ru3Sprujzs/s1600-h/tomcat.png
