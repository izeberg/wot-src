package net.wg.story_mode.battle.views.intro.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class IntroVideoVO extends DAAPIDataClass
   {
       
      
      public var skipButtonLabel:String = "";
      
      public var loadingText:String = "";
      
      public var loadingImage:String = "";
      
      public var video:String = "";
      
      public var isPausedAfterLoad:Boolean = false;
      
      public function IntroVideoVO(param1:Object)
      {
         super(param1);
      }
   }
}
