// DwarfMgr.java
import java.util.*;
import Database;
import DbRowSet;

public class DwarfMgr {
  private static String select = "select d.dwarf_id as dwarfid,d.dwarf_name as dwarfname,d.born as born,d.home_id as homeid,m.mountain_name as homename,d.spouse_id as spouseid,s.dwarf_name as spousename from dwarf d left join dwarf s on d.spouse_id = s.dwarf_id left join mountain m on d.home_id = m.mountain_id";

  private static String singleSelect = "select d.dwarf_id as dwarfid,d.dwarf_name as dwarfname,d.born as born,d.home_id as homeid,m.mountain_name as homename,d.spouse_id as spouseid,s.dwarf_name as spousename from dwarf d left join dwarf s on d.spouse_id = s.dwarf_id left join mountain m on d.home_id = m.mountain_id " + "  where d.dwarf_id = ?";

  //--------------------------------------------------------------
  public static List GetAll() throws java.sql.SQLException {
    DbRowSet res = Database.RunSql(select);
    List ret = new LinkedList();

    while(res.next()){
      Dwarf d = new Dwarf(res.getInt("dwarfid"),res.getString("dwarfname"),res.getInt("born"),res.getInt("homeid"),res.getString("homename"),res.getInt("spouseid"),res.getString("spousename"));
      ret.add(d);
    } 

    return ret;
  } 

  //--------------------------------------------------------------
  public static Dwarf Get(int id) throws java.sql.SQLException {
    List params = new LinkedList();
    params.add(new Integer(id));
    DbRowSet res = Database.RunSql(singleSelect,params);
    Dwarf d = null;

    while(res.next()){
      d = new Dwarf(res.getInt("dwarfid"),res.getString("dwarfname"),res.getInt("born"),res.getInt("homeid"),res.getString("homename"),res.getInt("spouseid"),res.getString("spousename"));
    }

    return d;
  } 

  //--------------------------------------------------------------
  public static int Add(String dwarfName,int born,int homeId) throws java.sql.SQLException
  {
    List params = new LinkedList();
    params.add(dwarfName);
if(born!= 0) params.add(new Integer(born)); else params.add(null);
if(homeId!= 0) params.add(new Integer(homeId)); else params.add(null);

    Database.RunSql("insert into dwarf (dwarf_name,born,home_id) values ( ?,?,?)", params);

    // return id later...
    return 0;
  }

  //--------------------------------------------------------------
  public static void Update(int id,
                        String dwarfName,int born,int homeId) throws java.sql.SQLException
  {
    List params = new LinkedList();
    params.add(dwarfName);
if(born!= 0) params.add(new Integer(born)); else params.add(null);
if(homeId!= 0) params.add(new Integer(homeId)); else params.add(null);

    params.add(new Integer(id));

    Database.RunSql("update dwarf set dwarf_name = ? ,born = ? ,home_id = ?  where dwarf_id = ? ", params);
  }
}

