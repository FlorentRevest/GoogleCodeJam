with Ada.Text_IO;           use Ada.Text_IO;
with Ada.Integer_Text_IO;   use Ada.Integer_Text_IO;
with Ada.Strings;           use Ada.Strings;
with Ada.Strings.Fixed;     use Ada.Strings.Fixed;

procedure filefixit is
    ----------------------------- Types definition -----------------------------
    -- Node helps representing a tree structure. Ptr_Node is a pointer to Node
    type Node ;
    type Ptr_Node is access Node ;
    
    type Node_Array is array (integer range <>) of Ptr_Node;
    type Ptr_Node_Array is access Node_Array;
    
    type Node is record 
        Name : String(1..100);
        Subdirectories_Array : Ptr_Node_Array;
    end record;

    -------------------------------- Functions ---------------------------------
    -- This procedure searches for the first directory of a path
    -- e.g: It returns the position of the substring "a" for "/a/b/c/d"
    procedure First_Dir_Of_Path(Path : String; Found : out boolean ; Starting, Ending : out positive) is
        i : Natural := Path'First;
    begin
        Found := false;

        -- Skip the first / if any
        while i < Path'Last loop
            exit when Path(i) /= '/';
            i := i+1;
        end loop;
        if i < Path'Last then
            Starting := i;
            Found := true;              -- TODO: WTF WTF WTF WTF WTF WTF ALWAYS TRUE -> Stack Overflow
        else
            return;
        end if;

        while i < Path'Last loop
            exit when Path(i) = '/';
            i := i+1;
        end loop;
        if i < Path'Last then
            Ending := i-1;
        else
            Ending := i;
        end if;
    end First_Dir_Of_Path;

    -- This procedure recursively creates Nodes for the given Directory
    -- It also increments the Mkdir_Nb variable every time it creates a new Node
    procedure Add_Node(Directory : in out Node; Path : String; Mkdir_Nb : in out Natural) is
        Found :boolean;
        Starting ,ending:positive;
        
        Old_Subdirectories_Array : Ptr_Node_Array;
        Subdir_Exists: Boolean := false;
    begin
        First_Dir_Of_Path(Path, Found, Starting, Ending);
        if found then  -- found <- if there is a first directory in the path
            for i in Directory.Subdirectories_Array'Range loop
                if Path(Starting..Ending) = Directory.Subdirectories_Array.all(i).name then
                    Add_Node(Directory.Subdirectories_Array.all(i).all, Path(Ending..Path'Last), Mkdir_Nb);
                    Subdir_Exists := true;
                    exit;
                end if;
            end loop;
            if not Subdir_Exists then
                Old_Subdirectories_Array := Directory.Subdirectories_Array;
                Directory.Subdirectories_Array := new Node_array(old_subdirectories_array.all'first..old_subdirectories_array.all'last+1) ;
                for i in old_subdirectories_array.all'range loop
                    directory.subdirectories_array.all(i):=old_subdirectories_array.all(i);
                end loop;
                directory.subdirectories_array.all(directory.subdirectories_array.all'last):= new node'((others => ' '), new node_array(1..0));
                directory.subdirectories_array.all(directory.subdirectories_array.all'last).all.name(directory.subdirectories_array.all(directory.subdirectories_array.all'last).all.name'First..directory.subdirectories_array.all(directory.subdirectories_array.all'last).all.name'First+(ending-starting)) := path(starting..ending);
                mkdir_nb:=mkdir_nb+1;
                Add_Node(directory.subdirectories_array.all(directory.subdirectories_array.all'last).all, directory.subdirectories_array.all(directory.subdirectories_array.all'last).all.name, Mkdir_Nb);
            end if;
        end if;
    end;

    Tests_Nb : Natural := 0;
    length : integer;
begin
    Ada.Integer_Text_IO.Get(Tests_Nb);
    for Test in 1..Tests_Nb loop -- For each test, create a root node that we will populate
        declare
            Root_Node       : Node    := ((others => ' '), new node_array(1..0));
            Existing_Dir_Nb : Natural := 0;
            New_Dir_Nb      : Natural := 0;
            Mkdir_Nb        : Natural := 0;
            New_Path        : String(1..100);
        begin
            Ada.Integer_Text_IO.Get(Existing_Dir_Nb);
            Ada.Integer_Text_IO.Get(New_Dir_Nb);

            --- HHHHAAAACCKKKKKKK 
            Ada.Text_IO.Get_Line(New_Path, length);

            for i in 1..Existing_Dir_Nb loop -- For each existing dir, populate the tree
                Ada.Text_IO.Get_Line(New_Path, length);
                Add_Node(Root_Node, New_Path, Mkdir_Nb);
            end loop;
            
            Mkdir_Nb := 0; -- We overwrite Mkdir_Nb because we only want the Mkdir_Nb of new directories
            for i in 1..New_Dir_Nb loop     -- For each new directory, populate the tree and get the Mkdir_Nb
                Ada.Text_IO.Get_Line(New_Path, length);
                Add_Node(Root_Node, New_Path, Mkdir_Nb);
            end loop;
            -- And show the number of mkdir commands that was needed
            Ada.Text_IO.Put_Line("Case #" & Ada.Strings.Fixed.Trim(Natural'Image(Test), Ada.Strings.Left) & ":" & Natural'Image(Mkdir_Nb));
        end;
    end loop;
end filefixit;
