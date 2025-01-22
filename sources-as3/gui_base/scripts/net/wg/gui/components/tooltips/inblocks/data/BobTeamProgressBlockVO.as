package net.wg.gui.components.tooltips.inblocks.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class BobTeamProgressBlockVO extends DAAPIDataClass
   {
       
      
      public var team:String = "";
      
      public var progress:String = "";
      
      public var place:String = "";
      
      public var isHighlighted:Boolean = false;
      
      public var isLikeHidden:Boolean = false;
      
      public function BobTeamProgressBlockVO(param1:Object)
      {
         super(param1);
      }
   }
}
