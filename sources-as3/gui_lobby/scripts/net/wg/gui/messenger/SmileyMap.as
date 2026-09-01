package net.wg.gui.messenger
{
   import flash.text.TextField;
   import net.wg.gui.utils.ImageSubstitution;
   import scaleform.gfx.TextFieldEx;
   
   public class SmileyMap
   {
       
      
      private var map:Vector.<ImageSubstitution> = null;
      
      public function SmileyMap()
      {
         super();
         var _loc1_:Number = 9;
         var _loc2_:Number = 4;
         var _loc3_:String = "smiley_happy";
         var _loc4_:String = "smiley_hmm";
         var _loc5_:String = "smiley_mad";
         var _loc6_:String = "smiley_madah";
         var _loc7_:String = "smiley_norm";
         var _loc8_:String = "smiley_oh";
         var _loc9_:String = "smiley_sad";
         var _loc10_:String = "smiley_tongue";
         var _loc11_:String = "smiley_wink";
         var _loc12_:String = "smiley_kiss";
         this.map = Vector.<ImageSubstitution>([new ImageSubstitution(":)",_loc3_,_loc1_,16,16,true,_loc2_),new ImageSubstitution("=)",_loc3_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":-)",_loc3_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":\\",_loc4_,_loc1_,16,16,true,_loc2_),new ImageSubstitution("=\\",_loc4_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":-\\",_loc4_,_loc1_,16,16,true,_loc2_),new ImageSubstitution("=/",_loc4_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":-/",_loc4_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(">:|",_loc5_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(">=|",_loc5_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(">:-|",_loc5_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(">:O",_loc6_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(">=O",_loc6_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(">:-O",_loc6_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(">:o",_loc6_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(">=o",_loc6_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(">:-o",_loc6_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(">:0",_loc6_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(">=0",_loc6_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(">:-0",_loc6_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":|",_loc7_,_loc1_,16,16,true,_loc2_),new ImageSubstitution("=|",_loc7_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":-|",_loc7_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":O",_loc8_,_loc1_,16,16,true,_loc2_),new ImageSubstitution("=O",_loc8_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":-O",_loc8_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":o",_loc8_,_loc1_,16,16,true,_loc2_),new ImageSubstitution("=o",_loc8_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":-o",_loc8_,_loc1_,16,16,true,_loc2_),new ImageSubstitution("=0",_loc8_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":-0",_loc8_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":(",_loc9_,_loc1_,16,16,true,_loc2_),new ImageSubstitution("=(",_loc9_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":-(",_loc9_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":P",_loc10_,_loc1_,16,16,true,_loc2_),new ImageSubstitution("=P",_loc10_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":-P",_loc10_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":*",_loc12_,_loc1_,16,16,true,_loc2_),new ImageSubstitution("=*",_loc12_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(":-*",_loc12_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(";)",_loc11_,_loc1_,16,16,true,_loc2_),new ImageSubstitution(";-)",_loc11_,_loc1_,16,16,true,_loc2_)]);
      }
      
      public function mapText(param1:TextField) : void
      {
         var _loc2_:ImageSubstitution = null;
         for each(_loc2_ in this.map)
         {
            TextFieldEx.setImageSubstitutions(param1,_loc2_);
         }
      }
   }
}
