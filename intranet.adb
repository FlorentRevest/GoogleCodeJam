with Ada.Text_IO, Ada.Integer_Text_IO, Ada.Strings.Fixed;

procedure intranet is
    type T_Wire is record 
        Right_floor : Integer ;
        Left_Floor : Integer ;
    end record ;

    type T_Wires_Array is array(Natural range <>) of T_Wire ;

    --see two lines are intersected or not 
    function Intersected (Wire1,Wire2 : T_Wire ) return Boolean is 
        Result:Boolean:=False;
    begin
        if (Wire1.Right_Floor < Wire2.right_Floor and Wire1.Left_Floor > Wire2.Left_Floor)
            or (Wire1.Right_Floor > Wire2.Right_Floor and Wire1.Left_Floor < Wire2.Left_Floor) then
            Result:=True;
        end if;
        return Result;
    end Intersected;

    --count how many intersected point between two buildings
    function Count(N:T_Wires_array) return Natural is
        Nb:integer:=0;
    begin
        for I in N'first..N'Last loop
            if I /= N'Last then
                for j in I+1..N'last loop
                    if Intersected(N(I),N(J)) = True then
                        Nb:=Nb+1;
                    end if ;
                end loop;
            end if ;
        end loop;
        return Nb;
    end Count ;

    Tests_Nb : Natural := 0;
    Wires_Nb : Natural := 0;
begin
    Ada.Integer_Text_IO.Get(Tests_Nb);
    for Test in 1..Tests_Nb loop -- For each test
        Ada.Integer_Text_IO.Get(Wires_Nb);
        declare                  -- Fill a wires array
            Wires_Array : T_Wires_Array(1..Wires_Nb);
        begin
            for i in Wires_Array'Range loop
                Ada.Integer_Text_IO.Get(Wires_Array(i).Left_Floor);
                Ada.Integer_Text_IO.Get(Wires_Array(i).Right_Floor);
            end loop;

            -- And show the number of intersections
            Ada.Text_IO.Put_Line("Case #" & Ada.Strings.Fixed.Trim(Natural'Image(test), Ada.Strings.Left) & ":" & Natural'Image(Count(Wires_Array)));
        end ;
    end loop;
end intranet;
