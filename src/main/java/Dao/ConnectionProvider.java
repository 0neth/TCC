/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Dao;
import Bean.Buyer;
import java.sql.*;    
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;
/**
 *
 * @author pedro
 */
public class ConnectionProvider {
    public static Connection getCon() throws SQLException{
        try {
            Class.forName("org.postgresql.Driver");
            Connection con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/GerenciadorDeDividas","postgres","kunga7");
            return con;
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(ConnectionProvider.class.getName()).log(Level.SEVERE, null, ex);
            return null;  
        }          
    }

    //create read update & delete -> crud
public class Crud{
    public static void update(Buyer buyer) throws SQLException{
        Connection con=ConnectionProvider.getCon();
        String sql = "UPDATE buyer SET name = ? , cellphone = ?, email = ? , address = ?, gender = ? where cpf = ? ";
        PreparedStatement pst = con.prepareStatement(sql);
        pst.setString(1,buyer.getName() );
        pst.setString(2,buyer.getCellphone() );
        pst.setString(3,buyer.getEmail() );
        pst.setString(4,buyer.getAddress() );
        pst.setString(5,buyer.getGender() );
        pst.setString(6,buyer.getCPF());
        pst.executeUpdate();
        }
    
    
    
    public static Buyer search(Buyer buyer) throws SQLException{
        Connection con=ConnectionProvider.getCon();
        String sql = ("SELECT * FROM buyer WHERE cpf =(?)");
        PreparedStatement pst = con.prepareStatement(sql);            
        pst.setString(1,buyer.getCPF());            
        ResultSet rs=pst.executeQuery(); 
        if(rs.next()){
            buyer.setName(rs.getString(2));
            buyer.setCellphone(rs.getString(3));
            buyer.setEmail(rs.getString(4));
            buyer.setAddress(rs.getString(5));
            buyer.setGender(rs.getString(6));        
            }else{
                JOptionPane.showMessageDialog(null,"CPF não existe");
            }
        return buyer;
        }
    }
}